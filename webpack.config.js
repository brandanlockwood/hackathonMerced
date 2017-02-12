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
                presets:['es2015', 'react', 'stage-0']
              }
            },
            { test: /\.css$/,
              loader: 'style-loader!css-loader'
            }
        ]
    },
    plugins: [
      new webpack.NoEmitOnErrorsPlugin()
    ]

};
