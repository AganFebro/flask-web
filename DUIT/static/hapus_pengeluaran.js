  function deleteNote(noteId1) {
    fetch("/delete-note-pengeluaran", {
      method: "POST",
      body: JSON.stringify({ noteId1: noteId1 }),
    }).then((_res) => {
      window.location.href = "/pengeluaran";
    });
  }