import tempfile
import webbrowser

def main(text, title="Alert"):
    with tempfile.NamedTemporaryFile(
        mode="w", suffix=".html", delete=False
    ) as home:
        html = f"""
            <html>
                <head>
                    <title>{title}</title>
                </head>
                <body>
                    <h1>
                        {text}
                    </h1>
                </body>
            </html>
        """
        home.write(html)
        path = "file://" + home.name
    webbrowser.open(path)
