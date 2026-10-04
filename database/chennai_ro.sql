DROP DATABASE IF EXISTS chennai_ro;

CREATE DATABASE chennai_ro;

USE chennai_ro;


-- =========================================================
-- USERS TABLE
-- =========================================================

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- PRODUCTS TABLE
-- =========================================================

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price DECIMAL(10,2) NOT NULL,
    image VARCHAR(255) NOT NULL DEFAULT 'placeholder.jpg',
    category VARCHAR(100),
    capacity VARCHAR(50),
    technology VARCHAR(150),
    stock INT DEFAULT 0,
    featured BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- ORDERS TABLE
-- =========================================================

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL,
    phone VARCHAR(20),
    address TEXT,
    total_amount DECIMAL(10,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_orders_user
    FOREIGN KEY (user_id)
    REFERENCES users(id)
    ON DELETE SET NULL
);


-- =========================================================
-- ORDER ITEMS TABLE
-- =========================================================

CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    product_name VARCHAR(200),
    price DECIMAL(10,2),
    quantity INT NOT NULL,
    subtotal DECIMAL(10,2),

    CONSTRAINT fk_order_items_order
    FOREIGN KEY (order_id)
    REFERENCES orders(id)
    ON DELETE CASCADE,

    CONSTRAINT fk_order_items_product
    FOREIGN KEY (product_id)
    REFERENCES products(id)
    ON DELETE CASCADE
);


-- =========================================================
-- SERVICE REQUESTS TABLE
-- =========================================================

CREATE TABLE service_requests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    phone VARCHAR(20),
    service_type VARCHAR(100),
    message TEXT,
    status VARCHAR(50) DEFAULT 'Pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- CONTACTS TABLE
-- =========================================================

CREATE TABLE contacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(150),
    phone VARCHAR(20),
    subject VARCHAR(200),
    message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- =========================================================
-- PRODUCTS
-- =========================================================

INSERT INTO products
(name, description, price, image, category, capacity, technology, stock, featured)
VALUES

(
'AquaPure Smart RO',
'Advanced RO water purifier for modern homes with multi-stage purification.',
12999,
'2.jpg',
'RO Purifier',
'8 L',
'7 Stage RO',
10,
TRUE
),

(
'AquaPure RO Max',
'High performance RO purifier with advanced purification technology.',
14499,
'3.jpg',
'RO Purifier',
'8 L',
'8 Stage RO',
8,
TRUE
),

(
'PureFlow RO Elite',
'Premium RO purifier designed for clean and safe drinking water.',
16999,
'4.jpg',
'RO Purifier',
'10 L',
'RO + UV + UF',
7,
TRUE
),

(
'AquaFresh UV+UF',
'Compact UV and UF water purification system.',
7499,
'5.jpg',
'UV Purifier',
'7 L',
'UV + UF',
12,
FALSE
),

(
'PureLife Compact RO',
'Space-saving RO purifier for apartments and small families.',
8999,
'6.jpg',
'RO Purifier',
'7 L',
'RO + UV',
10,
FALSE
),

(
'AquaShield RO Plus',
'Reliable RO purifier with multiple purification stages.',
13499,
'7.jpg',
'RO Purifier',
'8 L',
'RO + UV + UF',
9,
TRUE
),

(
'HydroPure 8L RO',
'8 litre household RO purifier.',
11999,
'8.jpg',
'RO Purifier',
'8 L',
'RO + UV',
10,
FALSE
),

(
'AquaPrime 10L RO',
'Large capacity RO purifier for families.',
15999,
'9.jpg',
'RO Purifier',
'10 L',
'RO + UV + UF',
8,
TRUE
),

(
'PureDrop RO Advanced',
'Advanced purification system with premium filtration.',
17499,
'10.jpg',
'RO Purifier',
'10 L',
'9 Stage RO',
6,
TRUE
),

(
'AquaCare RO Classic',
'Affordable RO purifier for everyday household use.',
9999,
'11.jpg',
'RO Purifier',
'8 L',
'6 Stage RO',
15,
FALSE
),

(
'CrystalPure RO',
'Crystal-clear water purification system.',
13999,
'12.jpg',
'RO Purifier',
'8 L',
'RO + UV',
9,
FALSE
),

(
'AquaMax Copper RO',
'Premium RO purifier with copper enrichment.',
18499,
'13.jpg',
'RO Purifier',
'10 L',
'RO + UV + Copper',
5,
TRUE
),

(
'HydroCare UV Purifier',
'Compact UV purification system.',
6999,
'14.jpg',
'UV Purifier',
'7 L',
'UV + UF',
12,
FALSE
),

(
'AquaGuard Home RO',
'Home RO purification solution.',
12499,
'15.jpg',
'RO Purifier',
'8 L',
'RO + UV',
10,
FALSE
),

(
'PureWave RO Pro',
'Professional grade household RO purifier.',
16499,
'16.jpg',
'RO Purifier',
'10 L',
'8 Stage RO',
7,
TRUE
),

(
'AquaPlus 7 Stage RO',
'7 stage RO purification for safe drinking water.',
13999,
'17.jpg',
'RO Purifier',
'8 L',
'7 Stage RO',
9,
FALSE
),

(
'CrystalFlow RO',
'Premium water purification with advanced filters.',
14999,
'18.jpg',
'RO Purifier',
'8 L',
'RO + UV + UF',
8,
TRUE
),

(
'PureWater 8L RO',
'Affordable 8 litre RO purifier.',
10999,
'19.jpg',
'RO Purifier',
'8 L',
'RO + UV',
11,
FALSE
),

(
'AquaLife RO',
'Reliable water purification for families.',
11499,
'20.jpg',
'RO Purifier',
'8 L',
'6 Stage RO',
10,
FALSE
),

(
'HydroFresh RO',
'Fresh and purified drinking water system.',
12999,
'21.jpg',
'RO Purifier',
'8 L',
'RO + UV',
9,
FALSE
),

(
'AquaSmart Digital RO',
'Smart digital RO purifier with modern controls.',
18999,
'22.jpg',
'RO Purifier',
'10 L',
'RO + UV + UF',
5,
TRUE
),

(
'PureShield RO',
'Advanced protection from impurities.',
15499,
'23.jpg',
'RO Purifier',
'10 L',
'8 Stage RO',
7,
TRUE
),

(
'AquaHome Compact',
'Compact purifier for small spaces.',
8499,
'24.jpg',
'RO Purifier',
'7 L',
'RO + UV',
13,
FALSE
),

(
'Crystal Aqua RO',
'Elegant and efficient RO purifier.',
13499,
'25.jpg',
'RO Purifier',
'8 L',
'RO + UV',
9,
FALSE
),

(
'HydroPure Premium',
'Premium high-capacity RO purifier.',
19999,
'26.jpg',
'RO Purifier',
'10 L',
'9 Stage RO',
4,
TRUE
),

(
'AquaZen RO',
'Modern RO purifier for home use.',
14999,
'27.jpg',
'RO Purifier',
'8 L',
'RO + UV + UF',
8,
FALSE
),

(
'PureFlow 9 Stage',
'9 stage advanced purification system.',
16999,
'28.jpg',
'RO Purifier',
'10 L',
'9 Stage RO',
6,
TRUE
),

(
'AquaFresh Premium',
'Premium household water purifier.',
17999,
'29.jpg',
'RO Purifier',
'10 L',
'RO + UV + UF',
6,
TRUE
),

(
'HydroMax RO',
'Powerful RO purification system.',
15999,
'30.jpg',
'RO Purifier',
'10 L',
'8 Stage RO',
8,
FALSE
),

(
'PureLife Advanced',
'Advanced purification for families.',
13999,
'31.jpg',
'RO Purifier',
'8 L',
'RO + UV',
9,
FALSE
),

(
'AquaCare Premium',
'Premium RO purifier with advanced filtration.',
18999,
'32.jpg',
'RO Purifier',
'10 L',
'9 Stage RO',
5,
TRUE
),

(
'RO Membrane Filter',
'Replacement RO membrane filter.',
899,
'33.jpg',
'Filter',
'Universal',
'RO Membrane',
30,
FALSE
),

(
'Sediment Filter',
'Replacement sediment filter cartridge.',
499,
'34.jpg',
'Filter',
'Universal',
'Sediment Filter',
40,
FALSE
),

(
'Carbon Filter Cartridge',
'High quality carbon filter cartridge.',
699,
'35.jpg',
'Filter',
'Universal',
'Carbon Filter',
35,
FALSE
),

(
'RO Pre Filter Kit',
'Complete RO pre-filter replacement kit.',
999,
'36.jpg',
'Filter',
'Universal',
'Pre Filter',
25,
FALSE
),

(
'Inline Filter Set',
'Inline water filter replacement set.',
799,
'37.jpg',
'Filter',
'Universal',
'Inline Filter',
30,
FALSE
),

(
'Mineral Cartridge',
'Mineral enhancement cartridge.',
899,
'38.jpg',
'Filter',
'Universal',
'Mineral Filter',
25,
FALSE
),

(
'Post Carbon Filter',
'Replacement post-carbon filter.',
649,
'39.jpg',
'Filter',
'Universal',
'Post Carbon',
35,
FALSE
),

(
'RO Filter Combo Kit',
'Complete RO filter replacement combo.',
1499,
'40.jpg',
'Filter',
'Universal',
'Multi Filter',
20,
TRUE
);


-- =========================================================
-- CHECK DATABASE
-- =========================================================

SELECT COUNT(*) AS total_products
FROM products;

SELECT id, name, price, image, featured
FROM products
LIMIT 10;

SHOW TABLES;
ERROR 1317 (70100): Query execution was interrupted
ALTER TABLE products ADD featured BOOLEAN DEFAULT FALSE;
