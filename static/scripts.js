function confirmDelete() {
    if(confirm("Are you sure you would like to remove your account? This will remove the account irreversibly.")) {
        window.location.href = "/delete_carrier"; 
    } else {
        // User clicked cancel, do nothing
    }
}