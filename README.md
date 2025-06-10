# LiveAEVI - AI Platform Clone

A full-stack web application clone of LiveAEVI AI platform built with vanilla HTML, CSS, JavaScript frontend and Flask backend with PostgreSQL database.

## Features

### Frontend
- **Responsive Design**: Mobile-first approach with smooth animations
- **Modern UI**: Gradient backgrounds, hover effects, and micro-interactions
- **Smooth Scrolling**: Navigation with animated scroll to sections
- **Contact Form**: Interactive form with validation and submission
- **Newsletter Signup**: Email subscription functionality
- **Performance Optimized**: Lazy loading and efficient animations

### Backend (Flask)
- **RESTful API**: Clean API endpoints for all functionality
- **Database Integration**: PostgreSQL with SQLAlchemy ORM
- **Contact Management**: Store and manage contact form submissions
- **Newsletter System**: Email subscription management
- **User Authentication**: Login/registration system with bcrypt
- **Analytics Tracking**: Basic page view tracking
- **Admin Panel**: Admin user management (API only)

## Tech Stack

### Frontend
- HTML5
- CSS3 (Flexbox, Grid, Animations)
- Vanilla JavaScript (ES6+)
- Google Fonts (Inter)

### Backend
- Flask (Python web framework)
- SQLAlchemy (ORM)
- PostgreSQL (Database)
- Flask-CORS (Cross-origin requests)
- bcrypt (Password hashing)
- python-dotenv (Environment variables)

## Setup Instructions

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Node.js (optional, for development)

### Database Setup
1. Install PostgreSQL and create a database:
```bash
createdb liveaevi_db
```

2. Run the database setup script:
```bash
psql -d liveaevi_db -f database_setup.sql
```

### Backend Setup
1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```

3. Run the Flask application:
```bash
python app.py
```

The backend will be available at `http://localhost:5000`

### Frontend Setup
1. Open `index.html` in a web browser, or
2. Serve it with a simple HTTP server:
```bash
python -m http.server 8000
```

## API Endpoints

### Contact Management
- `POST /api/contact` - Submit contact form
- `GET /api/contacts` - Get all contacts (with pagination)
- `PUT /api/contacts/<id>` - Update contact status

### Newsletter
- `POST /api/newsletter` - Subscribe to newsletter
- `GET /api/newsletter/subscribers` - Get all subscribers

### Authentication
- `POST /api/register` - Register new user
- `POST /api/login` - User login

### Analytics
- `POST /api/analytics/track` - Track page visit
- `GET /api/analytics/stats` - Get analytics statistics

### Utility
- `GET /api/health` - Health check endpoint

## Database Schema

### Users
- id, username, email, password_hash, is_admin, created_at, last_login

### Contacts
- id, name, email, company, message, created_at, status

### Newsletter
- id, email, subscribed_at, is_active

### Analytics
- id, page_url, user_agent, ip_address, referrer, timestamp

## Features

### Responsive Design
- Mobile-first approach
- Breakpoints: 768px (tablet), 480px (mobile)
- Flexible grid layouts
- Touch-friendly navigation

### Animations
- Smooth scroll to sections
- Fade-in animations on scroll
- Hover effects on interactive elements
- Loading states for forms

### Security
- Password hashing with bcrypt
- CORS configuration
- Input validation
- SQL injection prevention with ORM

### Performance
- Lazy loading for images
- Efficient CSS animations
- Minimal JavaScript footprint
- Optimized database queries

## Customization

### Styling
Edit `styles.css` to customize:
- Color scheme (CSS variables)
- Typography and spacing
- Animation timings
- Responsive breakpoints

### Content
Edit `index.html` to update:
- Text content and copy
- Images and media
- Section structure
- Meta information

### Backend
Edit `app.py` to add:
- New API endpoints
- Additional database models
- Business logic
- Third-party integrations

## Production Deployment

### Environment Variables
Set these in production:
```
DATABASE_URL=postgresql://user:pass@host:port/dbname
SECRET_KEY=your-super-secret-key
FLASK_ENV=production
```

### Database
- Use a managed PostgreSQL service
- Enable SSL connections
- Set up regular backups
- Configure connection pooling

### Security
- Change default admin password
- Use HTTPS in production
- Set up proper CORS origins
- Enable rate limiting
- Use environment variables for secrets

### Performance
- Use a reverse proxy (Nginx)
- Enable gzip compression
- Set up CDN for static assets
- Configure database indexing
- Monitor application performance

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).