// product.js

document.addEventListener("DOMContentLoaded", function () {
    // Get the Cart button and add a click event listener
    const cartButton = document.querySelector('.btn-cart');
    if (cartButton) {
        cartButton.addEventListener('click', handleCartButtonClick);
    }

    // Get all Add to Cart buttons and add click event listeners
    const addToCartButtons = document.querySelectorAll('.buy-now-button');
    addToCartButtons.forEach(button => {
        button.addEventListener('click', handleAddToCartButtonClick);
    });
});

// Function to handle Cart button click
function handleCartButtonClick(event) {
    event.preventDefault();
    alert("Cart button clicked!");
    // You can add more functionality here, e.g., open a modal or navigate to the Cart page
}

// Function to handle Add to Cart button click
function handleAddToCartButtonClick(event) {
    event.preventDefault();
    const productId = event.currentTarget.dataset.productId; // Get the product ID from the button's data attribute
    alert("Add to Cart button clicked for product ID: " + productId);
    // You can send an AJAX request to add the product to the cart or perform other actions
    // Update the cart count, etc.
}
