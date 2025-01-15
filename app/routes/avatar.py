from flask import Blueprint, render_template

avatar_bp = Blueprint("avatar", __name__)

@avatar_bp.route("/avatar")
def avatar():
    """
    Rendering avatar visualization page
    """
    return render_template("avatar.html")
