<?php include '../includes/header.php'; ?>

<h1>Add Product</h1>

<form method="POST" enctype="multipart/form-data">
    <input type="text" name="name" placeholder="Product Name"><br>
    <input type="number" name="price" placeholder="Price"><br>
    <input type="file" name="image"><br>
    <button type="submit">Add Product</button>
</form>

<?php include '../includes/footer.php'; ?>
