from flask import Flask, render_template, request

app = Flask(__name__)

def render_dynamic_layout(layout_order):
    # Dictionary to map container names to their respective HTML files
    container_files = {
        'header': 'header.html',
        'center': 'center.html',
        'br': 'br.html',
        'footer': 'footer.html'
    }
    
    # List to store the content of each container
    containers = []
    
    # Read the content of each container file based on the layout order
    for container in layout_order:
        if container in container_files:
            file_path = f'templates/{container_files[container]}'
            try:
                with open(file_path, 'r') as file:
                    containers.append(file.read())
            except FileNotFoundError:
                print(f"Warning: {file_path} not found. Skipping this container.")
        else:
            print(f"Warning: Unknown container '{container}'. Skipping.")
    
    # Render the index template with the dynamically ordered containers
    return render_template('index.html', containers=containers)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'layout1' in request.form:
            return render_dynamic_layout(['header', 'br', 'center', 'br', 'footer'])
        if 'layout2' in request.form:
            return render_dynamic_layout(['header', 'br', 'footer'])
        if 'layout3' in request.form:
            return render_dynamic_layout(['header', 'br', 'center', 'br', 'center', 'br', 'footer'])
            
    return render_dynamic_layout(['header', 'center', 'footer'])

if __name__ == '__main__':
    app.run(debug=True)