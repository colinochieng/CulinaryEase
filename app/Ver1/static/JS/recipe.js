window.addEventListener("load", function() {
    const ingredientsContainer = document.getElementById("ingredients-container");
    const addIngredientButton = document.getElementById("add-ingredient");
    let ingredientCount = 1;

    function createIngredientInput() {
    const ingredientInput = document.createElement("div");
    ingredientInput.classList.add("ingredients");
    ingredientInput.innerHTML = `
    <input type="text"  name="ingredient_name${ingredientCount}" placeholder="Description and name" maxlength="60" required>
    <input type="number" name="amount${ingredientCount}" placeholder="amount" min="0" required>
    <input type="text" name="unit${ingredientCount}" placeholder="measuring unit" list="measures-authorized" required>
    <input type="number" name="cost${ingredientCount}" placeholder="Cost @Unit" min="0" required>
    <button class="delete-ingredient">Delete</button>
    `;
      ingredientsContainer.appendChild(ingredientInput);
      ingredientCount++;
      const deleteButton = ingredientInput.querySelector(".delete-ingredient");
      deleteButton.addEventListener("click", () => {
        ingredientsContainer.removeChild(ingredientInput);
      });
    }
    
    addIngredientButton.addEventListener("click", createIngredientInput);

    /*
    Updating the total cook time when preparation time and cook time are updated
    */
    const prepTimeInput = document.getElementById('prep_time');
    const cookTimeInput = document.getElementById('cook_time');
    const totalTimeInput = document.getElementById('total_time');

    function updateTotalTime() {
      const prepTime = parseFloat(prepTimeInput.value) || 0;
      const cookTime = parseFloat(cookTimeInput.value) || 0;
      const total = prepTime + cookTime;
      
      totalTimeInput.value = total;
    }

    prepTimeInput.addEventListener('input', updateTotalTime);
    cookTimeInput.addEventListener('input', updateTotalTime);


    //autocomplition
    document.querySelectorAll('input').forEach(function(value, number) {
      value.setAttribute('autocomplete', 'on');
    });
    document.querySelectorAll('textarea').forEach((value, number) => {
      value.setAttribute('autocomplete', 'on');
    });
  });

