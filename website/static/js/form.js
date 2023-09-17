// Displays/disables (organizer/sponsor) form with provided ID
function displayForm(formId, visible) {
    var form = document.getElementById(formId);
    if (visible) {
        form.style = "display: block; z-index: 999; position: fixed;";
    } else {
        form.style = "display: none;"
    }
}

// Name is pretty straightforward.
function displayDashboard(dashId) {
    const dashboards = ["volunteerDash", "organizerDash", "sponsorDash"];
    for (let i = 0; i < dashboards.length; i++) {
        if (dashboards[i] != dashId) {
            document.getElementById(dashboards[i]).style = "display: none;";
        }
    }
    document.getElementById(dashId).style = "display: block;";
}

function transferDataToEventModal() {

}

function transferDataToItemModal(element, x, y) {
    displayForm(x, y);
    for (const child of element.children) {
        console.log(child);
        if (child.className == "description") {
            document.getElementById("description-m").innerText = child.innerText;
        }
    }
}

console.log("Javascript loaded! LOLZ")