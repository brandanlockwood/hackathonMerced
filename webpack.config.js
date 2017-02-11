const webpack = require('webpack'); 

module.exports = {
    // decided to do a single page app so we have only 1 entry
    entry: [
      './js/app.js'
    ],
    output: {
        path: __dirname + '/build',
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { test: /\.js?$/,
              loader: 'babel-loader',
              exclude: /node_modules/,
              query:
              {
                presets:['es2015', 'react']
              }
            },
            { test: /\.css$/, loader: "style!css" }
        ]
    },
    plugins: [
      new webpack.NoEmitOnErrorsPlugin()
    ]

};
