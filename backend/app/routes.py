# Get all products
@main.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([
        {
            'id': p.id,
            'name': p.name,
            'description': p.description,
            'price': p.price,
            'image_url': p.image_url
        } for p in products
    ])

# Get one product
@main.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify({
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': product.price,
        'image_url': product.image_url
    })

# Add to cart
@main.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.get_json()
    item = CartItem(user_id=data['user_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(item)
    db.session.commit()
    return jsonify({'message': 'Item added to cart'})

# View cart
@main.route('/cart/<int:user_id>', methods=['GET'])
def view_cart(user_id):
    items = CartItem.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            'item_id': i.id,
            'product_name': i.product.name,
            'quantity': i.quantity,
            'price_each': i.product.price,
            'total': i.quantity * i.product.price
        } for i in items
    ])

# Remove from cart
@main.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_cart_item(item_id):
    item = CartItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return jsonify({'message': 'Item removed'})

# Place order
@main.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    cart_items = CartItem.query.filter_by(user_id=data['user_id']).all()

    for item in cart_items:
        order = Order(
            user_id=item.user_id,
            product_id=item.product_id,
            quantity=item.quantity,
            total_price=item.quantity * item.product.price
        )
        db.session.add(order)
        db.session.delete(item)  # clear cart
    db.session.commit()

    return jsonify({'message': 'Order placed successfully'})

# View orders
@main.route('/orders/<int:user_id>', methods=['GET'])
def view_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            'product': o.product.name,
            'quantity': o.quantity,
            'total': o.total_price
        } for o in orders
    ])
