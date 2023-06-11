```sql
create database myshop;
ALTER DATABASE myshop CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
use database;

CREATE TABLE users (
id INT PRIMARY KEY AUTO_INCREMENT,
name CHAR(20) NOT NULL,
password CHAR(30) NOT NULL,
phone CHAR(20) NOT NULL,
address CHAR(100) NOT NULL,
gender ENUM('男', '女') NOT NULL
);
INSERT INTO users (name, password, phone, address, gender)
VALUES
  ('张三', '123456', '1234567890', '中国北京市', '男'),
  ('李四', '123456', '9876543210', '中国上海市', '女'),
  ('王五', '123456', '5551234567', '中国广州市', '男'),
  ('赵六', '123456', '1112223333', '中国深圳市', '女'),
  ('钱七', '123456', '4445556666', '中国天津市', '男'),
  ('孙八', '123456', '7778889999', '中国重庆市', '女'),
  ('周九', '123456', '3332221111', '中国成都市', '男'),
  ('吴十', '123456', '9998887777', '中国武汉市', '女'),
  ('郑一', '123456', '6667778888', '中国南京市', '男'),
  ('王二', '123456', '2223334444', '中国杭州市', '女'),
  ('陈十一', '123456', '8889990000', '中国苏州市', '男'),
  ('朱十二', '123456', '7776665555', '中国宁波市', '女'),
  ('刘十三', '123456', '4443332222', '中国青岛市', '男'),
  ('杨十四', '123456', '1112223333', '中国大连市', '女'),
  ('黄十五', '123456', '6665554444', '中国厦门市', '男'),
  ('何十六', '123456', '9998887777', '中国珠海市', '女'),
  ('吕十七', '123456', '3334445555', '中国三亚市', '男'),
  ('曾十八', '123456', '8887776666', '中国香港特别行政区', '女'),
  ('冯十九', '123456', '7776665555', '中国澳门特别行政区', '男'),
  ('严二十', '123456', '4445556666', '中国台北市', '女');

```

```sql
CREATE TABLE admins (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name CHAR(20) NOT NULL,
  password CHAR(30) NOT NULL
) AUTO_INCREMENT = 1000;

INSERT INTO admins (name, password)
VALUES
  ('童恩伟', 'admin123'),
  ('管理员', 'admin123');

```

```sql
CREATE TABLE products (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name CHAR(20) NOT NULL,
  stock INT NOT NULL,
  product_price DECIMAL(10, 2) NOT NULL,
  discounted_price DECIMAL(10, 2)
  information TEXT
);

DELIMITER //
CREATE TRIGGER init_discounted_price
BEFORE INSERT ON products
FOR EACH ROW
BEGIN
    SET NEW.discounted_price = NEW.product_price;
END //
DELIMITER ;

INSERT INTO products (name, stock, product_price, information)
VALUES
  ('联想拯救者',100,8999,'为拯救而生'),
  ('华为P70',50,7999,'国产之光'),
  ('时间简史',100,20,'探索时间的奥秘'),
  ('充电宝',40,200.0,'华为充电宝'),
  ('百乐钢笔',10,100.5,'比肩晨光'),
  ('滑板', 10, 99.99, '这是一款高品质的滑板，适合街头运动爱好者。'),
  ('衣服', 20, 49.99, '这是一件时尚舒适的衣服，适合各种场合穿着。'),
  ('零食', 15, 4.99, '这是一款美味可口的零食，让您享受美食时光。'),
  ('家具', 12, 199.99, '这是一件精心设计的家具，为您的家居增添风格和舒适感。'),
  ('鞋子', 5, 79.99, '这是一双时尚耐穿的鞋子，让您走在时尚尖端。'),
  ('书籍', 18, 29.99, '这是一本知识丰富的书籍，带给您知识与乐趣。'),
  ('美妆产品', 9, 39.99, '这是一款高品质的美妆产品，让您散发自信与美丽。'),
  ('运动器材', 25, 149.99, '这是一款专业级的运动器材，助您提升运动表现。'),
  ('手表', 30, 199.99, '这是一款时尚精致的手表，展现您的品味与风格。'),
  ('手机', 40, 699.99, '这是一款功能强大的智能手机，满足您的通信和娱乐需求。'),
  ('相机', 15, 299.99, '这是一款高性能的数码相机，让您捕捉美好瞬间。'),
  ('手提包', 25, 89.99, '这是一款时尚实用的手提包，方便您携带物品。'),
  ('玩具', 30, 19.99, '这是一款逗趣有趣的玩具，为孩子们带来快乐时光。'),
  ('音乐器材', 10, 399.99, '这是一款优质的音乐器材，让您享受音乐创作与演奏。'),
  ('厨具', 20, 49.99, '这是一套实用耐用的厨具，帮助您烹饪美食。'),
  ('健身器材', 8, 499.99, '这是一款专业级的健身器材，助您塑造健美身材。'),
  ('电脑配件', 12, 79.99, '这是一款优质的电脑配件，提升电脑性能和体验。'),
  ('家居装饰', 22, 29.99, '这是一款精美的家居装饰品，为您的家添加温馨氛围。'),
  ('游戏机', 5, 499.99, '这是一台强大的游戏机，畅玩各种精彩游戏。'),
   ('手套', 15, 9.99, '这是一双保暖舒适的手套，适用于冬季户外活动。'),
  ('耳机', 20, 39.99, '这是一款高音质的耳机，提供沉浸式音乐体验。'),
  ('眼镜', 8, 29.99, '这是一副时尚的眼镜，保护您的眼睛并增添个人魅力。'),
  ('宠物用品', 12, 19.99, '这是一些宠物用品，满足您宠物的需求和关爱。'),
  ('画笔', 25, 4.99, '这是一套优质的画笔，适用于绘画和艺术创作。'),
  ('床上用品', 30, 49.99, '这是一套舒适的床上用品，提供优质的睡眠体验。'),
  ('运动鞋', 10, 89.99, '这是一双专业运动鞋，为您的运动提供舒适和支持。'),
  ('香水', 18, 59.99, '这是一款迷人的香水，散发出独特的香气。'),
  ('手表', 22, 149.99, '这是一款精致的手表，彰显您的品味和个性。'),
  ('图书', 5, 24.99, '这是一本知识丰富的图书，带给您阅读的乐趣和启发。'),
  ('雷蛇电竞鼠标',1,1000,'雷蛇出品，品质保证');
```

```sql
CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT,
  total_price DECIMAL(10, 2),
  order_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE order_items (
  item_id INT PRIMARY KEY AUTO_INCREMENT,
  order_id INT,
  product_id INT,
  quantity INT,
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

CREATE TABLE cart (
  user_id INT,
  product_id INT,
  quantity INT,
  PRIMARY KEY (user_id, product_id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

```



```sql
CREATE TABLE discounts (
  product_id INT NOT NULL,
  discount DECIMAL(10, 2) NOT NULL,
  end_time DATETIME NOT NULL,
  FOREIGN KEY (product_id) REFERENCES products(id)
);

DELIMITER //
CREATE TRIGGER update_discounted_price
AFTER INSERT ON discounts
FOR EACH ROW
UPDATE products
SET discounted_price = product_price * (1 - NEW.discount)
WHERE id = NEW.product_id;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER modify_discounted_price
AFTER UPDATE ON discounts
FOR EACH ROW
UPDATE products
SET discounted_price = product_price * (1 - NEW.discount)
WHERE id = NEW.product_id;
//
DELIMITER ;

DELIMITER //
CREATE TRIGGER restore_original_price
AFTER DELETE ON discounts
FOR EACH ROW
UPDATE products
SET discounted_price = product_price
WHERE id = OLD.product_id;
//
DELIMITER ;

DELIMITER //
CREATE EVENT delete_expired_discounts
ON SCHEDULE EVERY 1 DAY
DO
DELETE FROM discounts
WHERE end_time < NOW();
//
DELIMITER ;


INSERT INTO discounts (product_id, discount, end_time)
VALUES
(1, 0.1, '2023-05-31 23:59:59'),
(2, 0.2, '2023-05-31 23:59:59'),
(3, 0.3, '2023-05-31 23:59:59');

delete from discounts where product_id = 2;
UPDATE discounts SET discount = 0.2, end_time = '2023-06-01 23:59:59' WHERE product_id = 1;
```

```sql
CREATE VIEW product_discounts AS
SELECT p.id, p.name, p.stock, p.product_price, p.discounted_price, d.end_time, p.information
FROM products p
LEFT JOIN discounts d ON p.id = d.product_id;

CREATE VIEW cart_products AS
SELECT c.user_id, c.product_id, p.name, p.discounted_price, c.quantity,p.stock, p.discounted_price * c.quantity AS total_price, c.quantity * (p.product_price - p.discounted_price) AS saved_solo
FROM cart c
LEFT JOIN products p ON p.id = c.product_id;

CREATE VIEW orderitem_products AS
SELECT oi.order_id, oi.product_id, p.name, p.discounted_price, oi.quantity, oi.quantity * p.discounted_price AS total_price
FROM order_items AS oi
LEFT JOIN products AS p ON oi.product_id = p.id
```

