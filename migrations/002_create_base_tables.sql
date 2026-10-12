create table customers (
	id varchar(26) primary key
	, name varchar (255) not null
	, phone varchar (100) not null
	, email varchar (255) null
	, created_at text not null default CURRENT_TIMESTAMP
	, deleted_at text null
);

create table products (
	id varchar(26) primary key
	, name varchar (255) not null
	, code varchar (100) not null
	, price integer not null
	, deleted_at text null
);

create table orders (
	id varchar(26) primary key
	, customer_id varchar(26) not null
	, status varchar (30) not null
	, delivery_date text null
	, remarks text null
	, created_at text not null default CURRENT_TIMESTAMP
	, updated_at text not null
	, deleted_at text null
	, constraint fk_orders_customer foreign key (customer_id) references customers (id)
	, constraint enum_orders_status check (status in ('PENDING', 'PAYMENT_RECEIVED', 'ENROUTE', 'COMPLETE'))
);

create table order_items (
	order_id varchar(26) not null
	, product_id varchar(26) not null
	, quantity integer not null
	, total_price integer not null
	, primary key (order_id, product_id)
	, constraint fk_order_items_order foreign key (order_id) references orders (id)
	, constraint fk_order_items_product foreign key (product_id) references products (id)
	, constraint positive_order_items_quantity check (quantity > 0)
	, constraint positive_order_items_total_price check (total_price > 0)
);
