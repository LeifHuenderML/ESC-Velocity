from flask import Flask, request, redirect, url_for
import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go

class EscVelocity:
    def __init__(self):
        self.server = Flask(__name__)
        self.setup_routes()
        
    def setup_routes(self):
        @self.server.route('/', methods=['GET', 'POST'])
        def index():
            if request.method == 'POST':
                username = request.form['username']
                password = request.form['password']
                # Load user data from database
                df = {'leif': 'intellect', 'andrea': 'dragonballs'}
                # Check if user exists and password is correct
                if df.get(username) != password:
                    return 'Invalid username or password'
                
                # Redirect to dashboard
                return redirect(url_for('dashboard', username=username))
            
            return '''
                <form method="post">
                    Welcome to Esc Velocity!<br><br>
                    Please login to continue.<br><br>
                    Username: <input type="text" name="username"><br><br>
                    Password: <input type="password" name="password"><br><br>
                    <input type="submit" value="Login">
                </form>
            '''

        @self.server.route('/dashboard/')
        def dashboard():
            username = request.args.get('username')
            # Load user data from database
            if username == 'leif':
                df_path = 'df/leif_df.csv'
            elif username == 'andrea':
                df_path = 'df/andrea_df.csv'
        
            df = pd.read_csv(df_path)
            
            # Create a Plotly chart
            fig = px.line(df, x=df['Date'], y=['bp'], title='Daily Blood Pressure')
            graph_html = pio.to_html(fig, full_html=False)
            
            return f'''
                <h1>Welcome to the dashboard, {username}!</h1>
                <h2>Daily metric inputs</h2>
                <form method="post">
                    Blood Pressure: <input type="text" name="Blood Pressure"><br><br>
                    Blood Glucose: <input type="text" name="Blood Glucose"><br><br>
                    Blood Oxygen: <input type="text" name="Blood Oxygen"><br><br>
                    Body Weight: <input type="text" name="Body Weight"><br><br>
                    Sleep Duration: <input type="text" name="Sleep Duration"><br><br>
                    <input type="submit" value="Submit">
                </form>
                <br>
                <h2>Current Metrics</h2>
                {graph_html}
            '''

if __name__ == '__main__':
    app = EscVelocity()
    app.server.run(debug=True)
