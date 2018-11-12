import React, { Component } from 'react';
import { CommentList } from './components/commentList';
import { CommentBox } from './components/commentBox';
import '../scss/main.scss';

class App extends Component {
    render(){
      return (
        <div className="App">
          <h2>Comentários</h2>
          <CommentBox/>
          <hr />
          <CommentList />
        </div>
      )
    }
}

export default App;
