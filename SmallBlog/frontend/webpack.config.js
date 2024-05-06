const path = require("path");
const webpack = require("webpack");

module.exports = (env, argv) => {
    return {
        entry: "./src/index.jsx",
        output: {
            path: path.resolve(__dirname, "./static/frontend/js"),
            filename: "[name].js",
        },
        module: {
            rules: [
                {
                    test: /\.jsx$/,
                    exclude: /node_modules/,
                    use: {
                        loader: "babel-loader",
                        options: {
                            presets: ['@babel/preset-env', '@babel/preset-react']
                        }
                    },

                },
            ],
        },
        optimization: {
            minimize: true,
        },
        plugins: [
            new webpack.DefinePlugin({
                "process.env": {
                    // This has effect on the react lib size
                    NODE_ENV: JSON.stringify(argv.mode),
                },
            }),
        ]
    }

};