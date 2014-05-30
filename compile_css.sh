
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

lessc $DIR/_less/website/theme1_customization.less $DIR/css/stylesheet.min.css --yui-compress
