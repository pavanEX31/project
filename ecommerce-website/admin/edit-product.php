<?php include '../includes/header.php'; ?>

<h1>Edit Product</h1>

<?php
// fetch product logic
?>

<form method="POST" enctype="multipart/form-data">
    <input type="text" name="name" value=""><br>
    <input type="number" name="price" value=""><br>
    <input type="file" name="image"><br>
    <button type="submit">Update Product</button>
</form>

<?php include '../includes/footer.php'; ?>
