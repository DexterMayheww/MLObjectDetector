document.getElementById('fileInput').addEventListener('change', function(event) {
    const input = event.target;
    const preview = document.getElementById('imagePreview');
    const upload = document.getElementById('uploadArea');
    const imgContainer = document.getElementById('imageContainer');
    const clearButton = document.getElementById('clearButton');

    if (input.files && input.files[0]) {
      const reader = new FileReader();

      reader.onload = function(e) {
        preview.src = e.target.result;
        preview.style.display = 'block';
        upload.style.display = 'none';
        imgContainer.style.display = 'flex';
        clearButton.style.display = 'flex';
    };

      reader.readAsDataURL(input.files[0]);
    } else {
        preview.src = '#';
        preview.style.display = 'none';
        upload.style.display = 'block';
        imgContainer.style.display = 'none';
    }
});