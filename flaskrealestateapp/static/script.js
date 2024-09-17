



const filter = document.getElementById('filter-button');
filter.addEventListener('click', showHideFilter)

function showHideFilter(){
    const filter = document.getElementById("filter");
    if (filter.style.display === "none") {
        filter.style.display = "block";
      } else {
        filter.style.display = "none";
      }
}