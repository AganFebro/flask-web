function deleteNote(noteId) {
    fetch("/delete-note-pemasukan", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/pemasukan";
    });
  }