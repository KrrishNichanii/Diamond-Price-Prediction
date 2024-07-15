from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Retrieve form data
            carat = request.form.get('carat')
            depth = request.form.get('depth')
            table = request.form.get('table')
            x = request.form.get('x')
            y = request.form.get('y')
            z = request.form.get('z')
            cut = request.form.get('cut')
            color = request.form.get('color')
            clarity = request.form.get('clarity')

            # Check if any of the required fields are empty
            if not all([carat, depth, table, x, y, z, cut, color, clarity]):
                return render_template('form.html', final_result={"error":True , "msg" :'Error: All fields are required.'})

            # Convert values to appropriate types
            try:
                carat = float(carat)
                depth = float(depth)
                table = float(table)
                x = float(x)
                y = float(y)
                z = float(z)
            except ValueError:
                return render_template('form.html', final_result={"error": True ,"msg" :'Error: Invalid number format.'})

            # Ensure categorical fields have valid values if needed (add validation logic if needed)
            # For example, you might want to check if `cut`, `color`, and `clarity` are among valid categories
            # For simplicity, this example assumes they are valid if not empty

            # Create CustomData object
            data = CustomData(
                carat=carat,
                depth=depth,
                table=table,
                x=x,
                y=y,
                z=z,
                cut=cut,
                color=color,
                clarity=clarity
            )

            # Convert data to DataFrame
            final_new_data = data.get_data_as_dataframe()

            # Predict
            predict_pipeline = PredictPipeline()
            pred = predict_pipeline.predict(final_new_data)

            # Round result
            results = round(pred[0], 2)

            # Render result in the form template
            return render_template('form.html', final_result={"error":False , "msg":f"${results}"})
        
        except Exception as e:
            # Handle exceptions and display an error message
            return render_template('form.html', final_result={"error": True , "msg":'Error occurred: ' + str(e)})
    
    # Handle GET requests to show the form
    return render_template('form.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
