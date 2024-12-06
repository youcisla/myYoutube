const path = require('path');

module.exports = {
    entry: '../src/index.js',
    output: {
        path: path.resolve(__dirname, 'dist'),
        filename: 'bundle.js',
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader'],
            },
            {
                test: /\.(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                },
            },
        ],
    },
    resolve: {
        extensions: ['.js', '.jsx'],
        fallback: {
            "zlib": require.resolve("browserify-zlib"),
            "querystring": require.resolve("querystring-es3"),
            "stream": require.resolve("stream-browserify"),
            "path": require.resolve("path-browserify"),
            "crypto": require.resolve("crypto-browserify"),
            "fs": false, // Optional: Disable fs if not needed
            "os": require.resolve("os-browserify/browser"),
            "url": require.resolve("url"),
            "util": require.resolve("util"),
            "http": require.resolve("stream-http"),
            "net": false, // Optional: Disable net if not needed
        },
    },
    devServer: {
        static: {
            directory: path.join(__dirname, 'public'),
        },
        port: 3000,
        headers: {
            'Content-Type': 'application/javascript',
        },
    },
};
