
from flask import Flask, render_template, request, redirect, url_for, session
from datetime import date, datetime
from functools import wraps
import json

app = Flask(__name__)

from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector

app = Flask(__name__)

DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "9384289398",
    "database": "chennai_ro"
}

def get_db_connection():

    return mysql.connector.connect(
        host=DB_CONFIG["host"],
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"],
        database=DB_CONFIG["database"]
    )

# ============================================================
# FLASK CONFIGURATION
# ============================================================

app.secret_key = "chennai_ro_innovation_2026"

# ============================================================
# ADMIN LOGIN
# ============================================================

ADMIN_ID = "admin"
ADMIN_PASSWORD = "12345"


# ============================================================
# PRODUCTS
# ============================================================

PRODUCTS = [

    {
        "id": 1,
        "name": "AquaPure RO Supreme",
        "price": 12999,
        "category": "RO Purifier",
        "capacity": "8 Litres",
        "technology": "RO + UV + UF",
        "image": "1.PNG",
        "stock": 10
    },
{
    "id": 2,
    "name": "AquaPure RO Premium",
    "price": 14999,
    "category": "RO Purifier",
    "capacity": "10 Litres",
    "technology": "RO + UV + TDS",
    "image": "2.PNG",
    "stock": 8
},
    {
        "id": 3,
        "name": "AquaPure RO Pro",
        "price": 17999,
        "category": "RO Purifier",
        "capacity": "10 Litres",
        "technology": "RO + UV + UF + Copper",
        "image": "3.PNG",
        "stock": 12
    },
    {
        "id": 4,
        "name": "AquaPure Compact RO",
        "price": 9999,
        "category": "RO Purifier",
        "capacity": "7 Litres",
        "technology": "RO + UV",
        "image": "4.PNG",
        "stock": 15
    },
    {
        "id": 5,
        "name": "AquaPure Smart RO",
        "price": 15999,
        "category": "RO Purifier",
        "capacity": "8 Litres",
        "technology": "RO + UV + TDS",
        "image": "5.PNG",
        "stock": 10
    },
    {
        "id": 6,
        "name": "AquaPure Wall Mount",
        "price": 11499,
        "category": "RO Purifier",
        "capacity": "8 Litres",
        "technology": "RO + UF",
        "image": "6.PNG",
        "stock": 9
    },
    {
        "id": 7,
        "name": "AquaPure Copper Plus",
        "price": 18999,
        "category": "RO Purifier",
        "capacity": "10 Litres",
        "technology": "RO + UV + Copper",
        "image": "7.PNG",
        "stock": 7
    },
    {
        "id": 8,
        "name": "AquaPure TDS Control",
        "price": 16999,
        "category": "RO Purifier",
        "capacity": "9 Litres",
        "technology": "RO + UV + TDS",
        "image": "8.PNG",
        "stock": 11
    },
    {
        "id": 9,
        "name": "AquaPure Family RO",
        "price": 13999,
        "category": "RO Purifier",
        "capacity": "10 Litres",
        "technology": "RO + UV + UF",
        "image": "9.PNG",
        "stock": 10
    },
    {
        "id": 10,
        "name": "AquaPure Ultra RO",
        "price": 19999,
        "category": "RO Purifier",
        "capacity": "12 Litres",
        "technology": "RO + UV + Copper + TDS",
        "image": "10.PNG",
        "stock": 6
    },

    {
        "id": 11,
        "name": "RO Sediment Filter",
        "price": 499,
        "category": "Spare Parts",
        "capacity": "10 Inch",
        "technology": "Sediment Filtration",
        "image": "11.PNG",
        "stock": 25
    },
    {
        "id": 12,
        "name": "RO Carbon Filter",
        "price": 699,
        "category": "Spare Parts",
        "capacity": "10 Inch",
        "technology": "Activated Carbon",
        "image": "12.PNG",
        "stock": 20
    },
    {
        "id": 13,
        "name": "RO Membrane 100 GPD",
        "price": 999,
        "category": "Spare Parts",
        "capacity": "100 GPD",
        "technology": "RO Membrane",
        "image": "13.PNG",
        "stock": 20
    },
    {
        "id": 14,
        "name": "RO Membrane 75 GPD",
        "price": 899,
        "category": "Spare Parts",
        "capacity": "75 GPD",
        "technology": "RO Membrane",
        "image": "14.PNG",
        "stock": 20
    },
    {
        "id": 15,
        "name": "Premium Sediment Filter",
        "price": 599,
        "category": "Spare Parts",
        "capacity": "10 Inch",
        "technology": "5 Micron",
        "image": "15.PNG",
        "stock": 30
    },
    {
        "id": 16,
        "name": "Premium Carbon Filter",
        "price": 799,
        "category": "Spare Parts",
        "capacity": "10 Inch",
        "technology": "Carbon Block",
        "image": "16.PNG",
        "stock": 25
    },

    {
        "id": 17,
        "name": "RO Booster Pump",
        "price": 1499,
        "category": "Accessories",
        "capacity": "24V",
        "technology": "High Pressure Pump",
        "image": "17.PNG",
        "stock": 15
    },
    {
        "id": 18,
        "name": "RO Booster Pump Pro",
        "price": 1799,
        "category": "Accessories",
        "capacity": "36V",
        "technology": "High Pressure",
        "image": "18.PNG",
        "stock": 12
    },
    {
        "id": 19,
        "name": "Digital TDS Controller",
        "price": 1199,
        "category": "Accessories",
        "capacity": "Digital",
        "technology": "TDS Control",
        "image": "19.PNG",
        "stock": 15
    },
    {
        "id": 20,
        "name": "RO Water Tap",
        "price": 399,
        "category": "Accessories",
        "capacity": "Universal",
        "technology": "Food Grade",
        "image": "20.PNG",
        "stock": 30
    },
    {
        "id": 21,
        "name": "Premium RO Tap",
        "price": 599,
        "category": "Accessories",
        "capacity": "Universal",
        "technology": "Food Grade",
        "image": "21.PNG",
        "stock": 25
    },
    {
        "id": 22,
        "name": "RO Storage Tank",
        "price": 2499,
        "category": "Accessories",
        "capacity": "10 Litres",
        "technology": "Food Grade",
        "image": "22.PNG",
        "stock": 10
    },
    {
        "id": 23,
        "name": "RO Storage Tank Pro",
        "price": 2999,
        "category": "Accessories",
        "capacity": "12 Litres",
        "technology": "Food Grade",
        "image": "23.PNG",
        "stock": 8
    },

    {
        "id": 24,
        "name": "RO UV Lamp",
        "price": 799,
        "category": "Spare Parts",
        "capacity": "11 Watt",
        "technology": "UV Sterilization",
        "image": "24.PNG",
        "stock": 15
    },
    {
        "id": 25,
        "name": "RO UV Lamp Pro",
        "price": 999,
        "category": "Spare Parts",
        "capacity": "16 Watt",
        "technology": "UV Sterilization",
        "image": "25.PNG",
        "stock": 12
    },
    {
        "id": 26,
        "name": "RO SMPS Power Supply",
        "price": 699,
        "category": "Accessories",
        "capacity": "24V",
        "technology": "Power Supply",
        "image": "26.PNG",
        "stock": 20
    },
    {
        "id": 27,
        "name": "RO Solenoid Valve",
        "price": 499,
        "category": "Spare Parts",
        "capacity": "24V",
        "technology": "Automatic Valve",
        "image": "27.PNG",
        "stock": 20
    },
    {
        "id": 28,
        "name": "RO Flow Restrictor",
        "price": 299,
        "category": "Spare Parts",
        "capacity": "300 GPD",
        "technology": "Flow Control",
        "image": "28.PNG",
        "stock": 30
    },
    {
        "id": 29,
        "name": "RO Float Valve",
        "price": 349,
        "category": "Spare Parts",
        "capacity": "Universal",
        "technology": "Water Level Control",
        "image": "29.PNG",
        "stock": 30
    },
    {
        "id": 30,
        "name": "RO Pipe Set",
        "price": 449,
        "category": "Accessories",
        "capacity": "3 Metres",
        "technology": "Food Grade",
        "image": "30.PNG",
        "stock": 25
    },

    {
        "id": 31,
        "name": "RO Filter Set",
        "price": 1299,
        "category": "Filter Kit",
        "capacity": "Universal",
        "technology": "Multi Stage Filtration",
        "image": "31.PNG",
        "stock": 15
    },
    {
        "id": 32,
        "name": "RO Premium Filter Kit",
        "price": 1799,
        "category": "Filter Kit",
        "capacity": "Universal",
        "technology": "RO + Carbon + Sediment",
        "image": "32.PNG",
        "stock": 12
    },
    {
        "id": 33,
        "name": "RO Complete Service Kit",
        "price": 2299,
        "category": "Service Kit",
        "capacity": "Universal",
        "technology": "Complete Maintenance",
        "image": "33.PNG",
        "stock": 10
    },
    {
        "id": 34,
        "name": "RO Filter Replacement Kit",
        "price": 1499,
        "category": "Filter Kit",
        "capacity": "Universal",
        "technology": "Multi Stage",
        "image": "34.PNG",
        "stock": 15
    },
    {
        "id": 35,
        "name": "RO Installation Kit",
        "price": 999,
        "category": "Accessories",
        "capacity": "Universal",
        "technology": "Installation Kit",
        "image": "35.PNG",
        "stock": 15
    },
    {
        "id": 36,
        "name": "RO Maintenance Kit",
        "price": 1299,
        "category": "Service Kit",
        "capacity": "Universal",
        "technology": "Maintenance",
        "image": "36.PNG",
        "stock": 12
    },
    {
        "id": 37,
        "name": "RO Cleaning Kit",
        "price": 799,
        "category": "Service Kit",
        "capacity": "Universal",
        "technology": "Purifier Cleaning",
        "image": "37.PNG",
        "stock": 15
    },
    {
        "id": 38,
        "name": "RO Premium Accessories Kit",
        "price": 1999,
        "category": "Accessories",
        "capacity": "Universal",
        "technology": "Premium Accessories",
        "image": "38.PNG",
        "stock": 10
    },
    {
        "id": 39,
        "name": "Chennai RO Complete Kit",
        "price": 2499,
        "category": "Complete Kit",
        "capacity": "Universal",
        "technology": "Complete RO Solution",
        "image": "39.PNG",
        "stock": 10
    }
]


# ============================================================
# SAMPLE DATA
# ============================================================

# ============================================================
# TEMPORARY DATA
# ============================================================

ORDERS = []

SERVICE_REQUESTS = []

FEEDBACK_MESSAGES = []

_next_order_id = 1
_next_request_id = 1


# ============================================================
# HELPER
# ============================================================

def find_product(product_id):

    try:
        product_id = int(product_id)
    except (TypeError, ValueError):
        return None

    return next(
        (
            product
            for product in PRODUCTS
            if product["id"] == product_id
        ),
        None
    )


# ============================================================
# ADMIN PROTECTION
# ============================================================

def admin_required(function):

    @wraps(function)
    def decorated_function(*args, **kwargs):

        if not session.get("admin_logged_in"):

            return redirect(
                url_for("admin_login")
            )

        return function(*args, **kwargs)

    return decorated_function


# ============================================================
# HOME
# ============================================================

@app.route("/")
def index():

    return render_template(
        "index.html",
        active="home",
        featured_products=PRODUCTS[:6]
    )


# ============================================================
# PRODUCTS
# ============================================================

@app.route("/products")
def products():

    q = request.args.get(
        "q",
        ""
    ).strip().lower()

    category = request.args.get(
        "category",
        ""
    ).strip().lower()

    sort = request.args.get(
        "sort",
        ""
    ).strip()

    results = PRODUCTS.copy()

    # SEARCH

    if q:

        results = [
            p for p in results
            if q in p["name"].lower()
            or q in p["category"].lower()
            or q in p["technology"].lower()
        ]

    # CATEGORY

    category_map = {

        "ro": "RO Purifier",

        "parts": "Spare Parts",

        "accessories": "Accessories",

        "filter": "Filter Kit",

        "service": "Service Kit",

        "complete": "Complete Kit"
    }

    if category in category_map:

        results = [
            p
            for p in results
            if p["category"] == category_map[category]
        ]

    # SORT

    if sort == "price_asc":

        results = sorted(
            results,
            key=lambda p: p["price"]
        )

    elif sort == "price_desc":

        results = sorted(
            results,
            key=lambda p: p["price"],
            reverse=True
        )

    elif sort == "name_asc":

        results = sorted(
            results,
            key=lambda p: p["name"].lower()
        )

    return render_template(
        "products.html",
        active="products",
        products=results
    )


# ============================================================
# PRODUCT DETAILS
# ============================================================

@app.route("/product/<int:product_id>")
def product_details(product_id):

    product = find_product(product_id)

    if not product:

        return redirect(
            url_for("products")
        )

    return render_template(
        "product_details.html",
        active="products",
        product=product
    )
# ============================================================
# ADD TO CART
# ============================================================

@app.route("/add-to-cart/<int:product_id>")
def add_to_cart(product_id):

    product = find_product(product_id)

    if not product:
        return redirect(url_for("products"))

    cart = session.get("cart", {})

    product_key = str(product_id)

    current_quantity = int(cart.get(product_key, 0))

    # Check available stock
    if current_quantity >= product["stock"]:

        return redirect(url_for("products"))

    # Add product
    cart[product_key] = current_quantity + 1

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


# ============================================================
# CART
# ============================================================

@app.route("/cart")
def cart():

    session_cart = session.get("cart", {})

    cart_items = {}
    total = 0

    for product_id, quantity in session_cart.items():

        product = find_product(int(product_id))

        if not product:
            continue

        quantity = int(quantity)

        subtotal = product["price"] * quantity

        item = {
            "id": product["id"],
            "name": product["name"],
            "image": product["image"],
            "price": product["price"],
            "quantity": quantity,
            "subtotal": subtotal
        }

        cart_items[product_id] = item

        total += subtotal

    return render_template(
        "cart.html",
        cart=cart_items,
        total=total,
        active="cart"
    )


# ============================================================
# REMOVE FROM CART
# ============================================================

@app.route("/remove-from-cart/<int:product_id>")
def remove_from_cart(product_id):

    cart = session.get("cart", {})

    product_key = str(product_id)

    if product_key in cart:
        del cart[product_key]

    session["cart"] = cart
    session.modified = True

    return redirect(url_for("cart"))


# ============================================================
# CLEAR CART
# ============================================================

@app.route("/clear-cart")
def clear_cart():

    session["cart"] = {}

    session.modified = True

    return redirect(url_for("cart"))








# ============================================================
# CHECKOUT
# ============================================================


@app.route("/checkout", methods=["GET", "POST"])
def checkout():

    cart = session.get("cart", {})

    if not cart:
        return redirect(url_for("products"))

    cart_items = []
    total = 0

    for product_id, quantity in cart.items():

        product = find_product(int(product_id))

        if product:

            subtotal = float(product["price"]) * int(quantity)

            cart_items.append({
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "image": product["image"],
                "quantity": quantity,
                "subtotal": subtotal
            })

            total += subtotal

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        address = request.form.get("address", "").strip()

        if not name or not email or not phone or not address:
            return render_template(
                "checkout.html",
                cart=cart_items,
                total=total,
                error="Please fill all required fields.",
                active="cart"
            )

        # Send the order to your existing order function
        return redirect(url_for("place_order"))

    return render_template(
        "checkout.html",
        cart=cart_items,
        total=total,
        active="cart"
    )

# ============================================================
# PLACE ORDER
# ============================================================


# ============================================================
# ORDER SUCCESS
# ============================================================
@app.route("/place-order", methods=["POST"])
def place_order():

    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    address = request.form.get("address", "").strip()

    if not name or not email or not phone or not address:

        return redirect(url_for("checkout"))

    cart = session.get("cart", {})

    if not cart:
        return redirect(url_for("products"))

    total = 0

    validated_items = []

    for product_id, quantity in cart.items():

        product = find_product(int(product_id))

        if not product:
            continue

        quantity = int(quantity)

        if quantity <= 0:
            continue

        if quantity > product["stock"]:

            return render_template(
                "checkout.html",
                active="cart",
                total=total,
                error=f"Not enough stock for {product['name']}."
            )

        subtotal = float(product["price"]) * quantity

        total += subtotal

        validated_items.append({
            "product": product,
            "quantity": quantity
        })

    if not validated_items:
        return redirect(url_for("products"))

    connection = None
    cursor = None

    try:

        connection = get_db_connection()

        cursor = connection.cursor()

        user_id = session.get("user_id")

        sql = """
            INSERT INTO orders
            (
                user_id,
                customer_name,
                email,
                phone,
                address,
                total_amount,
                status
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """

        values = (
            user_id,
            name,
            email,
            phone,
            address,
            total,
            "Pending"
        )

        cursor.execute(sql, values)

        connection.commit()

        order_id = cursor.lastrowid

    except mysql.connector.Error as error:

        print("ORDER DATABASE ERROR:", error)

        if connection:
            connection.rollback()

        return render_template(
            "checkout.html",
            active="cart",
            total=total,
            error="Unable to place order. Please try again."
        )

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

    # Reduce stock
    for item in validated_items:

        product = item["product"]
        quantity = item["quantity"]

        product["stock"] -= quantity

    # Empty cart
    session["cart"] = {}

    session["order_success"] = (
        f"Order #{order_id} placed successfully!"
    )

    return redirect(url_for("order_success"))
@app.route("/order-success")
def order_success():

    message = session.pop(
        "order_success",
        "Your order was placed successfully."
    )

    return render_template(
        "index.html",
        active="home",
        featured_products=PRODUCTS[:6],
        success=message
    )


# ============================================================
# USER LOGIN
# ============================================================

@app.route(
    "/login",
    methods=["GET", "POST"]
)
def login():

    error = None

    if request.method == "POST":

        email = request.form.get(
            "email",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        ).strip()

        if not email or not password:

            error = (
                "Please enter email and password."
            )

        else:

            session["user_id"] = 1

            session["user_email"] = email

            return redirect(
                url_for("index")
            )

    return render_template(
        "login.html",
        active="login",
        error=error
    )


# ============================================================
# REGISTER
# ============================================================

@app.route(
    "/register",
    methods=["GET", "POST"]
)
def register():

    error = None

    if request.method == "POST":

        name = request.form.get(
            "name",
            ""
        ).strip()

        email = request.form.get(
            "email",
            ""
        ).strip()

        password = request.form.get(
            "password",
            ""
        ).strip()

        confirm = request.form.get(
            "confirm_password",
            ""
        ).strip()

        if not name or not email or not password:

            error = "Please fill all fields."

        elif password != confirm:

            error = "Passwords do not match."

        elif len(password) < 6:

            error = (
                "Password must contain at least 6 characters."
            )

        else:

            session["registered"] = True

            return redirect(
                url_for("login")
            )

    return render_template(
        "register.html",
        active="register",
        error=error
    )

# ============================================================
# USER LOGOUT
# ============================================================

@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for("index")
    )


@app.route("/service", methods=["GET", "POST"])
def service_request():

    global _next_request_id

    submitted = False
    error = None

    if request.method == "POST":

        print("================================")
        print("SERVICE FORM POST RECEIVED")
        print(request.form)
        print("================================")

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        phone = request.form.get("phone", "").strip()
        service_type = request.form.get("service_type", "").strip()
        address = request.form.get("address", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not phone or not service_type or not address or not message:

            error = "Please fill all required fields."

        else:

            SERVICE_REQUESTS.insert(
                0,
                {
                    "id": _next_request_id,
                    "customer": name,
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "type": service_type,
                    "service_type": service_type,
                    "address": address,
                    "message": message,
                    "status": "Pending"
                }
            )

            _next_request_id += 1

            submitted = True

            print("SERVICE REQUEST SAVED")
            print(SERVICE_REQUESTS[0])

    return render_template(
        "service.html",
        active="service_request",
        submitted=submitted,
        error=error
    )

# ============================================================
# CONTACT
# ============================================================

# ============================================================
# CONTACT
# ============================================================

@app.route("/contact", methods=["GET", "POST"])
def contact():

    submitted = False
    error = None

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email or not message:

            error = "Please fill all fields."

        else:

            connection = None
            cursor = None

            try:

                connection = get_db_connection()

                cursor = connection.cursor()

                cursor.execute("""
                    INSERT INTO contacts
                    (name, email, message)
                    VALUES (%s, %s, %s)
                """, (
                    name,
                    email,
                    message
                ))

                connection.commit()

                submitted = True

            except mysql.connector.Error as error:

                print("CONTACT DATABASE ERROR:", error)

                if connection:
                    connection.rollback()

                error = "Unable to send your message. Please try again."

            finally:

                if cursor:
                    cursor.close()

                if connection:
                    connection.close()

    return render_template(
        "contact.html",
        active="contact",
        submitted=submitted,
        error=error
    )

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():

    error = None

    if request.method == "POST":

        admin_id = request.form.get("admin_id", "").strip()
        admin_password = request.form.get("admin_password", "")

        if not admin_id or not admin_password:

            error = "Please enter Admin ID and Password."

        elif admin_id == ADMIN_ID and admin_password == ADMIN_PASSWORD:

            session["admin_logged_in"] = True
            session["admin_id"] = admin_id

            return redirect(url_for("admin_dashboard"))

        else:

            error = "Invalid Admin ID or Password."

    return render_template(
        "admin_login.html",
        error=error
    )


# ============================================================
# ADMIN DASHBOARD
# ============================================================

# ============================================================
# ADMIN DASHBOARD
# ============================================================

@app.route("/admin")
@admin_required
def admin_dashboard():

    connection = None
    cursor = None

    orders = []
    contact_messages = []

    try:

        connection = get_db_connection()

        cursor = connection.cursor(dictionary=True)

        # ----------------------------------------------------
        # GET ORDERS
        # ----------------------------------------------------

        cursor.execute("""
            SELECT
                id,
                customer_name,
                email,
                phone,
                address,
                DATE(created_at) AS date,
                total_amount AS total,
                status
            FROM orders
            ORDER BY id DESC
        """)

        orders = cursor.fetchall()

        # ----------------------------------------------------
        # GET CONTACT MESSAGES
        # ----------------------------------------------------

        cursor.execute("""
            SELECT
                id,
                name,
                email,
                message,
                created_at
            FROM contacts
            ORDER BY id DESC
        """)

        contact_messages = cursor.fetchall()

    except mysql.connector.Error as error:

        print("ADMIN DATABASE ERROR:", error)

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

    # --------------------------------------------------------
    # DASHBOARD CALCULATIONS
    # --------------------------------------------------------

    total_sales = sum(
        float(order["total"] or 0)
        for order in orders
        if order["status"] != "Cancelled"
    )

    total_orders = len(orders)

    total_products = len(PRODUCTS)

    low_stock = len([
        product
        for product in PRODUCTS
        if product["stock"] <= 5
    ])

    pending_orders = len([
        order
        for order in orders
        if order["status"] == "Pending"
    ])

    pending_services = len([
        service
        for service in SERVICE_REQUESTS
        if service["status"] == "Pending"
    ])

    # --------------------------------------------------------
    # SEND DATA TO ADMIN DASHBOARD
    # --------------------------------------------------------

    return render_template(
        "admin_dashboard.html",

        total_sales=total_sales,
        total_orders=total_orders,
        total_products=total_products,
        low_stock=low_stock,
        pending_orders=pending_orders,
        pending_services=pending_services,

        orders=orders,

        products=PRODUCTS,

        service_requests=SERVICE_REQUESTS,

        contact_messages=contact_messages
    )
# ============================================================
# ADMIN LOGOUT
# ============================================================

@app.route("/admin/logout")
def admin_logout():

    session.pop(
        "admin_logged_in",
        None
    )

    session.pop(
        "admin_id",
        None
    )

    return redirect(
        url_for("admin_login")
    )


# ============================================================
# ADMIN PRODUCT STOCK UPDATE
# ============================================================

@app.route(
    "/admin/product/<int:product_id>/stock",
    methods=["POST"]
)
@admin_required
def update_product_stock(product_id):

    product = find_product(
        product_id
    )

    if product:

        try:

            stock = int(
                request.form.get(
                    "stock",
                    product["stock"]
                )
            )

            if stock >= 0:

                product["stock"] = stock

        except (TypeError, ValueError):

            pass

    return redirect(
        url_for("admin_dashboard")
    )


# ============================================================
# ADMIN ORDER STATUS
# ============================================================

# ============================================================
# ADMIN ORDER STATUS - MYSQL
# ============================================================

@app.route(
    "/admin/order/<int:order_id>/status",
    methods=["POST"]
)
@admin_required
def update_order_status(order_id):

    new_status = request.form.get("status", "").strip()

    allowed_statuses = [
        "Pending",
        "Processing",
        "Delivered",
        "Cancelled"
    ]

    if new_status not in allowed_statuses:
        return redirect(url_for("admin_dashboard"))

    connection = None
    cursor = None

    try:

        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute(
            """
            UPDATE orders
            SET status = %s
            WHERE id = %s
            """,
            (new_status, order_id)
        )

        connection.commit()

    except mysql.connector.Error as error:

        print("ORDER STATUS ERROR:", error)

        if connection:
            connection.rollback()

    finally:

        if cursor:
            cursor.close()

        if connection:
            connection.close()

    return redirect(url_for("admin_dashboard"))

# ============================================================
# ADMIN SERVICE STATUS
# ============================================================

@app.route(
    "/admin/service/<int:request_id>/status",
    methods=["POST"]
)
@admin_required
def update_service_status(request_id):

    new_status = request.form.get(
        "status",
        ""
    ).strip()

    allowed_statuses = [
        "Pending",
        "Processing",
        "Completed",
        "Cancelled"
    ]

    if new_status in allowed_statuses:

        for service in SERVICE_REQUESTS:

            if service["id"] == request_id:

                service["status"] = new_status

                break

    return redirect(
        url_for("admin_dashboard")
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    print("")
    print("==========================================")
    print("       CHENNAI RO INNOVATION")
    print("==========================================")
    print("Flask server starting...")
    print("")
    print("Website:")
    print("http://127.0.0.1:5000")
    print("")
    print("Products:")
    print("http://127.0.0.1:5000/products")
    print("")
    print("Admin Login:")
    print("http://127.0.0.1:5000/admin/login")
    print("")
    print("Admin ID: admin")
    print("Admin Password: 12345")
    print("==========================================")
    print("")

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )