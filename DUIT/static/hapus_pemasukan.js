// function deleteNote(noteId) {
//     fetch("/delete-note-pemasukan", {
//       method: "POST",
//       body: JSON.stringify({ noteId: noteId }),
//     }).then((_res) => {
//       window.location.href = "/pemasukan";
//     });
//   }




// function deleteNote(noteId) {
//   var choice = confirm("Are you sure you want to delete this data?");
//   if (choice == true) {
//       fetch("/delete-note-pemasukan", {
//           method: "POST",
//           body: JSON.stringify({ noteId: noteId }),
//       }).then((_res) => {
//           window.location.href = "/pemasukan";
//       });
//   }
// }



function deleteNote(noteId) {
  // Show the confirm delete modal
  document.getElementById("confirm-delete-modal").style.display = "block";

  // Add event listener to the delete button in the modal
  document.getElementById("modal-delete-btn").addEventListener("click", function() {
      // Send the delete request and redirect to /pemasukan
      fetch("/delete-note-pemasukan", {
          method: "POST",
          body: JSON.stringify({ noteId: noteId }),
      }).then((_res) => {
          window.location.href = "/pemasukan";
      });
  });
  // Add event listener to the cancel button in the modal
  document.getElementById("modal-cancel-btn").addEventListener("click", function() {
  // Hide the modal
  document.getElementById("confirm-delete-modal").style.display = "none";
  });

  document.getElementById("confirm-delete-modal").addEventListener("click", function(event) {
    if (event.target == this) {
        this.style.display = "none";
    }
});

document.addEventListener("keydown", function(event) {
    if (event.keyCode == 27) {
        document.getElementById("confirm-delete-modal").style.display = "none";
    }
});
}