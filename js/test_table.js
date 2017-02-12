import React from 'react';
import ReactDOM from 'react-dom';
import {Table, Column, Cell} from 'fixed-data-table';
import FakeObjectDataListStore from './helpers/FakeObjectDataListStore';

const TextCell = ({rowIndex, data, col, ...props}) => (
  <Cell {...props}>
    {data.getObjectAt(rowIndex)[col]}
  </Cell>
);


const MyTable = class MyTable extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      dataList: new FakeObjectDataListStore(1000000),
    };

  }

  render() {
    let {dataList} = this.state;
    return (
      <div> TEST 
      
      <Table
        rowsCount={10}
        rowHeight={50}
        headerHeight={50}
        width={1000}
        height={500}>
        <Column
          header={<Cell>First Name</Cell>}
          cell={<TextCell data={dataList} col="firstName" />}
          width={200}
        />
      </Table>
      </div>
    );
  }
}

export default MyTable;



