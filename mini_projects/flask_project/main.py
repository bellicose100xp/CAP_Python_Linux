from typing import Any
from flask import Flask, render_template, request
from database import Database

# from sample_streams import sample_response
from watch_mode_api import WatchModeApi

app = Flask(__name__)
# app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search() -> dict[Any, Any]:
    query = request.args.get("q")
    assert query is not None
    db = Database()
    results = db.search_by_keyword("titles", "title", query)
    db.close()
    return {"results": results}  # return json


@app.route("/streams/<title_id>")
def streams(title_id: str) -> dict[Any, Any]:
    # Get sources from watch mode api
    watch_mode_api = WatchModeApi()
    sample_response = watch_mode_api.get_stream_sources(title_id)

    # Get image url from database for source network
    # Get flag url for region
    db = Database()
    for source in sample_response["sources"]:
        source["url"] = db.get_source_image(source["source_id"])
        source["flag_url"] = db.get_region_flag(source["region"])

    db.close()

    return render_template("streams.html", data=sample_response)  # type: ignore


if __name__ == "__main__":
    # Production
    app.run(host="0.0.0.0", port=2224, debug=True)

    # Development Only - use following versions
    # pip install livereload==2.5.1
    # pip install tornado<6.3.0
    # from livereload import Server  # type: ignore

    # app.debug = True  # required for template changes to show up via live-reload server
    # server = Server(app.wsgi_app)  # type: ignore
    # server.watch("templates/*.*")  # type: ignore
    # server.watch("static/*.*")  # type: ignore
    # server.serve(host="0.0.0.0", port=2224)  # type: ignore
