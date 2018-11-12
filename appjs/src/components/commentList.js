import React, { Component } from 'react';
import axios from 'axios';

class Comment extends Component {
  constructor(props) {
    super(props);
  }
  render(){
    return (
      <li id={`comment_${this.props.id}`} className="media comment">
        <div className="media-body">
          <h5 className="mt-0">{this.props.name}</h5>
          {this.props.text}
        </div>
      </li>
    );
  }
}

class CommentList extends Component {
  constructor(props) {
    super(props);
    this.state = { comments: [], page: 0 }
  }

  componentDidMount(){
    this.loadComments(this.state.page);
  }

  loadComments = (page) => {
    let url = `/comments/${window.article_id}`;
    axios.get(url, {
      params: {
        'page': page
      }
    }).then((response) => {
      this.setState({
        comments: [...this.state.comments, ...response.data.comments]
      })
    })
  }

  nextComments = () => {
    let page = this.state.page + 1;
    this.loadComments(page);
    this.setState({ page: page });
  }

  render(){
    const { comments } = this.state;
    return (
      <div>
        <div className="ListComments">
          <ul className="list-unstyled">
            {comments.map(comment => { return (<Comment id={comment.id} name={comment.name} text={comment.text}/>)})}
          </ul>
          <p><a href="javascript:void(0);" onClick={this.nextComments}>Ver mais comentários</a></p>
        </div>
      </div>
    );
  }
}

export { CommentList };
