const path = require('path');

module.exports = {
  entry: './src/index.js',
  output: {
    filename: 'e-widgets.v1.min.js',
    path: path.resolve(__dirname, 'dist'),
    clean: true
  },
  devServer: {
    static: {
      directory: path.join(__dirname, 'dist'),
    },
    compress: true,
    port: 9000,
  },
  watchOptions: {
    poll: 1000,
  },
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        loader: "babel-loader",
        options: {presets: ["@babel/preset-env", "@babel/preset-react"]}
      },
    ]
  }
};