const path = require('path');

module.exports = {
    mode: 'development',
    entry: './src/index.js', // Entry point
    output: {
        path: path.resolve(__dirname, 'dist'), // Output directory
        filename: 'bundle.js', // Output filename
    },
    module: {
        rules: [
            {
                test: /\.(js|jsx)$/, // Match both .js and .jsx files
                exclude: /node_modules/, // Exclude node_modules
                use: {
                    loader: 'babel-loader',
                },
            },
        ],
    },
    resolve: {
        extensions: ['.js', '.jsx'], // Allow importing without file extensions
    },
    devServer: {
        static: path.join(__dirname, 'public'), // Serve static files from public
        port: 3000, // Development server port
        hot: true, // Enable hot module replacement
    },
};
