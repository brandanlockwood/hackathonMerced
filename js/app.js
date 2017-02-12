import React from 'react';
import ReactDOM from 'react-dom';
import MyTable from './test_table';
import Header from './header';
import FilterMenu from './filtermenu';
//import Bootstrap from 'bootstrap/dist/css/bootstrap.min.css';

class App extends React.Component {
  render() {
    return (
      <div className="">
        <Header />
        <FilterMenu />
      </div>
    );
  }
}


ReactDOM.render(
  <App />,
  document.getElementById('root')
);

 