import React from 'react';
import ReactDOM from 'react-dom';
import { CommentList } from '../src/components/commentList';
import { CommentBox } from '../src/components/commentBox';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<CommentBox />, div);
  ReactDOM.unmountComponentAtNode(div);
});

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<CommentList />, div);
  ReactDOM.unmountComponentAtNode(div);
});
