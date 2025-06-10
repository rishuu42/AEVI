from flask import Flask, request, jsonify, render_template_string
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
import os
from dotenv import load_dotenv
import bcrypt

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://username:password@localhost/liveaevi_skincare_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'your-secret-key-here')

db = SQLAlchemy(app)

# Database Models
class Contact(db.Model):
    __tablename__ = 'contacts'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(100))
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='new')  # new, contacted, resolved
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'company': self.company,
            'message': self.message,
            'created_at': self.created_at.isoformat(),
            'status': self.status
        }

class Newsletter(db.Model):
    __tablename__ = 'newsletter'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subscribed_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'subscribed_at': self.subscribed_at.isoformat(),
            'is_active': self.is_active
        }

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    
    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password_hash.encode('utf-8'))
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat(),
            'last_login': self.last_login.isoformat() if self.last_login else None
        }

class Analytics(db.Model):
    __tablename__ = 'analytics'
    
    id = db.Column(db.Integer, primary_key=True)
    page_url = db.Column(db.String(255), nullable=False)
    user_agent = db.Column(db.String(500))
    ip_address = db.Column(db.String(45))
    referrer = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'page_url': self.page_url,
            'user_agent': self.user_agent,
            'ip_address': self.ip_address,
            'referrer': self.referrer,
            'timestamp': self.timestamp.isoformat()
        }

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.Float, nullable=False)
    original_price = db.Column(db.Float)
    image_url = db.Column(db.String(500))
    category = db.Column(db.String(100))
    is_featured = db.Column(db.Boolean, default=False)
    is_bestseller = db.Column(db.Boolean, default=False)
    is_new = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'original_price': self.original_price,
            'image_url': self.image_url,
            'category': self.category,
            'is_featured': self.is_featured,
            'is_bestseller': self.is_bestseller,
            'is_new': self.is_new,
            'created_at': self.created_at.isoformat()
        }

# Routes
@app.route('/')
def index():
    with open('index.html', 'r') as file:
        return render_template_string(file.read())

@app.route('/api/contact', methods=['POST'])
def contact():
    try:
        data = request.get_json()
        
        # Validate required fields
        if not data.get('name') or not data.get('email') or not data.get('message'):
            return jsonify({'error': 'Name, email, and message are required'}), 400
        
        # Create new contact entry
        contact = Contact(
            name=data['name'],
            email=data['email'],
            company=data.get('company', ''),
            message=data['message']
        )
        
        db.session.add(contact)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Contact form submitted successfully',
            'id': contact.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/newsletter', methods=['POST'])
def newsletter():
    try:
        data = request.get_json()
        
        if not data.get('email'):
            return jsonify({'error': 'Email is required'}), 400
        
        # Check if email already exists
        existing = Newsletter.query.filter_by(email=data['email']).first()
        if existing:
            if existing.is_active:
                return jsonify({'error': 'Email already subscribed'}), 400
            else:
                # Reactivate subscription
                existing.is_active = True
                existing.subscribed_at = datetime.utcnow()
                db.session.commit()
                return jsonify({
                    'success': True,
                    'message': 'Newsletter subscription reactivated'
                }), 200
        
        # Create new newsletter subscription
        newsletter = Newsletter(email=data['email'])
        db.session.add(newsletter)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Successfully subscribed to newsletter',
            'id': newsletter.id
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/products', methods=['GET'])
def get_products():
    try:
        featured_only = request.args.get('featured', 'false').lower() == 'true'
        category = request.args.get('category')
        
        query = Product.query
        
        if featured_only:
            query = query.filter_by(is_featured=True)
        
        if category:
            query = query.filter_by(category=category)
        
        products = query.order_by(Product.created_at.desc()).all()
        
        return jsonify({
            'products': [product.to_dict() for product in products]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    try:
        page = request.args.get('page', 1, type=int)
        per_page = request.args.get('per_page', 10, type=int)
        status = request.args.get('status')
        
        query = Contact.query
        
        if status:
            query = query.filter_by(status=status)
        
        contacts = query.order_by(Contact.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )
        
        return jsonify({
            'contacts': [contact.to_dict() for contact in contacts.items],
            'total': contacts.total,
            'pages': contacts.pages,
            'current_page': page
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/analytics/track', methods=['POST'])
def track_analytics():
    try:
        data = request.get_json()
        
        analytics = Analytics(
            page_url=data.get('page_url', ''),
            user_agent=request.headers.get('User-Agent', ''),
            ip_address=request.remote_addr,
            referrer=data.get('referrer', '')
        )
        
        db.session.add(analytics)
        db.session.commit()
        
        return jsonify({'success': True}), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/analytics/stats', methods=['GET'])
def get_analytics_stats():
    try:
        # Get basic stats
        total_visits = Analytics.query.count()
        today_visits = Analytics.query.filter(
            Analytics.timestamp >= datetime.utcnow().date()
        ).count()
        
        return jsonify({
            'total_visits': total_visits,
            'today_visits': today_visits,
            'total_contacts': Contact.query.count(),
            'newsletter_subscribers': Newsletter.query.filter_by(is_active=True).count(),
            'total_products': Product.query.count()
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'service': 'LiveAEVI Skincare API'
    }), 200

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500

# Initialize database and sample data
def init_database():
    db.create_all()
    
    # Create admin user if it doesn't exist
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(
            username='admin',
            email='admin@liveaevi.com',
            is_admin=True
        )
        admin.set_password('admin123')  # Change this in production
        db.session.add(admin)
        print("Admin user created: admin/admin123")
    
    # Add sample products if none exist
    if Product.query.count() == 0:
        sample_products = [
            Product(
                name='Vitamin C Brightening Serum',
                description='Advanced vitamin C formula that brightens and evens skin tone while providing antioxidant protection.',
                price=89.00,
                original_price=120.00,
                image_url='https://images.pexels.com/photos/3685530/pexels-photo-3685530.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop',
                category='serums',
                is_featured=True,
                is_bestseller=True
            ),
            Product(
                name='Retinol Renewal Night Cream',
                description='Gentle yet effective retinol cream that reduces fine lines and improves skin texture overnight.',
                price=125.00,
                image_url='https://images.pexels.com/photos/4465124/pexels-photo-4465124.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop',
                category='moisturizers',
                is_featured=True,
                is_new=True
            ),
            Product(
                name='Hyaluronic Hydra Moisturizer',
                description='Ultra-hydrating moisturizer with multiple types of hyaluronic acid for plump, dewy skin.',
                price=75.00,
                image_url='https://images.pexels.com/photos/4465831/pexels-photo-4465831.jpeg?auto=compress&cs=tinysrgb&w=400&h=400&fit=crop',
                category='moisturizers',
                is_featured=True
            )
        ]
        
        for product in sample_products:
            db.session.add(product)
        
        print("Sample products added")
    
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        init_database()
    
    app.run(host='0.0.0.0', port=5000, debug=True)