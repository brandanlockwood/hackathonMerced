import React, { Component, PropTypes } from 'react';
import { Panel, Button } from 'react-bootstrap';
import Checkbox from './checkbox';


const paneltitle = (
     <h3>Filters</h3>
);

export default class FilterMenu extends React.Component {
  render() {
    return (
        <Panel header={paneltitle}>
            <p>Color </p>
            <Checkbox label="red"/>
            <Checkbox label="blue"/>
            <Checkbox label="black"/>
            <Checkbox label="pink"/>
            <p>Clothing Categories</p>
            <Checkbox label="Tops"/>
            <Checkbox label="Jeans"/>
            <Checkbox label="Pants"/>
            <Checkbox label="Dresses"/>
            <p>Occasions</p>
            <Checkbox label="Casual"/>
            <Checkbox label="Work Event"/>
            <Checkbox label="Night Out"/>
            <Checkbox label="Wedding"/>
            <br />
            <Button bsStyle="primary" bsSize="large">Update Search</Button>
        </Panel>
    );
  }
}