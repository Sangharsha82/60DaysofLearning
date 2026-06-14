import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text, default='')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(app.instance_path, 'app.sqlite'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    if test_config:
        app.config.update(test_config)

    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError:
        pass

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        items = Item.query.order_by(Item.created_at.desc()).all()
        return render_template('index.html', items=items)

    @app.route('/add', methods=('GET', 'POST'))
    def add():
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            description = request.form.get('description', '').strip()
            if name:
                item = Item(name=name, description=description)
                db.session.add(item)
                db.session.commit()
                return redirect(url_for('index'))
        return render_template('add_item.html')

    @app.route('/<int:id>')
    def detail(id):
        item = Item.query.get_or_404(id)
        return render_template('detail.html', item=item)

    @app.route('/<int:id>/edit', methods=('GET', 'POST'))
    def edit(id):
        item = Item.query.get_or_404(id)
        if request.method == 'POST':
            name = request.form.get('name', '').strip()
            description = request.form.get('description', '').strip()
            if name:
                item.name = name
                item.description = description
                db.session.commit()
                return redirect(url_for('detail', id=item.id))
        return render_template('edit_item.html', item=item)

    @app.route('/<int:id>/delete', methods=('POST',))
    def delete(id):
        item = Item.query.get_or_404(id)
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('index'))

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
