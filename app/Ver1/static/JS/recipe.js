import { imgValidate } from "./validate.js";

window.addEventListener("load", function () {
  const ingredientsContainer = document.getElementById("ingredients-container");
  const addIngredientButton = document.getElementById("add-ingredient");
  let ingredientCount = 1;
  let ingredientCountTracker = [];

  function createIngredientInput() {
    const ingredientInput = document.createElement("div");
    ingredientInput.classList.add("ingredients");
    ingredientInput.innerHTML = `
    <input type="text"  name="ingredient_name${ingredientCount}" placeholder="Description and name" maxlength="60" required>
    <input type="number" name="amount${ingredientCount}" placeholder="amount" min="0" required>
    <input type="text" name="unit${ingredientCount}" placeholder="measuring unit" list="measures-authorized" required>
    <input type="text" name="cost${ingredientCount}" id="cost${ingredientCount}" placeholder="Cost @Unit" min="0" required>
    <button class="delete-ingredient" data-ingredient-count="${ingredientCount}">Delete</button>
    `;
    ingredientsContainer.appendChild(ingredientInput);
    ingredientCountTracker.push(ingredientCount);
    console.log(ingredientCountTracker);
    ingredientCount++;
    const deleteButton = ingredientInput.querySelector(".delete-ingredient");
    deleteButton.addEventListener("click", (event) => {
      const deletedCount = parseInt(
        event.target.getAttribute("data-ingredient-count")
      );
      ingredientCountTracker = ingredientCountTracker.filter(
        (item) => item != deletedCount
      );
      console.log(ingredientCountTracker);
      ingredientsContainer.removeChild(ingredientInput);
    });
  }

  addIngredientButton.addEventListener("click", createIngredientInput);

  /*
    Updating the total cook time when preparation time and cook time are updated
    */
  const prepTimeInput = document.getElementById("prep_time");
  const cookTimeInput = document.getElementById("cook_time");
  const totalTimeInput = document.getElementById("total_time");

  function updateTotalTime() {
    const prepTime = parseFloat(prepTimeInput.value) || 0;
    const cookTime = parseFloat(cookTimeInput.value) || 0;
    const total = prepTime + cookTime;

    totalTimeInput.value = total;
  }

  prepTimeInput.addEventListener("input", updateTotalTime);
  cookTimeInput.addEventListener("input", updateTotalTime);

  //autocomplition
  document.querySelectorAll("input").forEach(function (value, number) {
    value.setAttribute("autocomplete", "on");
  });
  document.querySelectorAll("textarea").forEach((value, number) => {
    value.setAttribute("autocomplete", "on");
  });

  /**
   * Ingredients costs checker
   * cost
   * Recipe image upload
   */
  let validateImagereturn;

  document
    .getElementById("user-recipe")
    .addEventListener("click", validateImagereturn = imgValidate("#user-recipe", "#imageFile"));

  document.addEventListener("DOMContentLoaded", () => {
    document
      .querySelector("#recipe-form")
      .addEventListener("submit", (event) => {
        event.preventDefault();

        if (validateImagereturn < 0) {
          alert('Wrong Image format Only png, jpg, jpeg or gif allowed');
        }

        ingredientCountTracker.forEach((value, index) => {
          let costInputElement = document.querySelector(
            `#cost${ingredientCount}`
          );
          const costValue = costInputElement.value;
          // Check if the input is a unit string (e.g., "25@kg")
          const isUnitString = /^[0-9]+@[a-zA-Z]+$/.test(costValue);

          if (isUnitString) {
            const cost = ParseInt(costValue);
            if (!cost) {
              alert(
                "Invalid Cost input. First part of the cost should an Integer"
              );
            } else {
              this.submit();
            }
          } else {
            alert(
              "Invalid Cost input. Maybe recheck your format e.g Cost@unit"
            );
          }
      });
      });
  });
});
