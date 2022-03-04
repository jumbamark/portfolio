let links = document.querySelectorAll(".scroll-to");
console.log(links);

links.forEach((item) => {
  item.addEventListener("click", () => {
    let section = document.getElementById(item.getAttribute("data-link"));
    section.scrollIntoView({behaviour: "smooth", block: "start"});
  });
});

// when the user clicks the link it scrolls to it's section - we use data-links instead of href in links
// adding event to the links, we need to make a loop to links-output to catch each link not all the links
// made a click event to each link
// will return all sections with the corresponding id
// save section id in let
// scrollInToView function in js takes two object and handles scroll in page
// we added data-link in attribute bec it's the attribute we used
// block takes four values - start, end, center, nearest
