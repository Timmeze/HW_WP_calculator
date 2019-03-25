from flask import Flask, request, render_template

from app.lib import wallpaper_calc


def main():
    app = Flask(__name__)


    @app.route('/')
    def front_calc():
        lenght = request.args.get('lenght')
        height = request.args.get('height')
        width = request.args.get('width')
        wallpaper_width = request.args.get('wallpaper_width')
        if lenght and height and width and wallpaper_width:
            res = wallpaper_calc(float(lenght), float(height), float(width), float(wallpaper_width))
            return render_template('calc.html', title="Wallpaper calculator", res=res, lenght=lenght, height=height, width=width, wallpaper_width=wallpaper_width)
        return render_template('calc.html', title="Wallpaper calculator",)

    app.run(port=9875, debug=True)

if __name__ == '__main__':
    main()
