from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for recipes (for simplicity)
recipes = []

@app.route('/')
def home():
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        recipes.append({'title': title, 'ingredients': ingredients, 'instructions': instructions})
        return redirect(url_for('home'))
    return render_template('add_recipe.html')

@app.route('/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    if recipe_id < len(recipes):
        recipes.pop(recipe_id)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)