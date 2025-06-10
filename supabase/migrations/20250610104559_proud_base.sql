-- LiveAEVI Database Schema
-- Run this script to set up the PostgreSQL database

-- Create database (run this as superuser)
-- CREATE DATABASE liveaevi_db;

-- Connect to the database and create tables
\c liveaevi_db;

-- Users table
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    is_admin BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP
);

-- Contacts table
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL,
    company VARCHAR(100),
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) DEFAULT 'new'
);

-- Newsletter table
CREATE TABLE IF NOT EXISTS newsletter (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120) UNIQUE NOT NULL,
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Analytics table
CREATE TABLE IF NOT EXISTS analytics (
    id SERIAL PRIMARY KEY,
    page_url VARCHAR(255) NOT NULL,
    user_agent VARCHAR(500),
    ip_address VARCHAR(45),
    referrer VARCHAR(255),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_contacts_created_at ON contacts(created_at);
CREATE INDEX IF NOT EXISTS idx_contacts_status ON contacts(status);
CREATE INDEX IF NOT EXISTS idx_newsletter_email ON newsletter(email);
CREATE INDEX IF NOT EXISTS idx_newsletter_active ON newsletter(is_active);
CREATE INDEX IF NOT EXISTS idx_analytics_timestamp ON analytics(timestamp);
CREATE INDEX IF NOT EXISTS idx_analytics_page_url ON analytics(page_url);
CREATE INDEX IF NOT EXISTS idx_users_username ON users(username);
CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);

-- Insert sample data (optional)
INSERT INTO users (username, email, password_hash, is_admin) VALUES
('admin', 'admin@liveaevi.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBgHxOJyKdxj2e', TRUE)
ON CONFLICT (username) DO NOTHING;

-- Sample newsletter subscribers
INSERT INTO newsletter (email) VALUES
('john@example.com'),
('sarah@techcompany.com'),
('mike@startup.io')
ON CONFLICT (email) DO NOTHING;

-- Sample contacts
INSERT INTO contacts (name, email, company, message) VALUES
('John Doe', 'john@example.com', 'TechCorp', 'Interested in your AI automation services.'),
('Sarah Johnson', 'sarah@innovate.com', 'Innovate Solutions', 'Would like to schedule a demo.'),
('Mike Chen', 'mike@dataflow.io', 'DataFlow Inc', 'Looking for enterprise pricing information.')
ON CONFLICT DO NOTHING;

COMMIT;