import React, { Component } from 'react';
import { getCookie } from '../utils/cookie';
import { withFormik } from 'formik';
import axios from 'axios';
import qs from 'qs';
import * as Yup from 'yup';

const validationSchema = Yup.object().shape({
  name: Yup.string().required('Por favor, entre com seu nome'),
  email: Yup.string().email('Por favor, entre com um e-mail válido').required('Por favor, entre com seu email'),
  text: Yup.string().required('Por favor, digite um texto :)')
});

const CommentForm = props => {
  const {
    values,
    touched,
    errors,
    dirty,
    isSubmitting,
    handleChange,
    handleBlur,
    handleSubmit,
    handleReset,
  } = props;
  return (
    <form action="comment" id="formComment" method="POST" onSubmit={handleSubmit}>
    <div className="form-row">
      <div className="form-group col-md-6">
        <input 
          type="text" 
          className="form-control" 
          name="name" 
          id="name" 
          value={values.name} 
          onChange={handleChange} 
          onBlur={handleBlur} 
          placeholder="Nome"/>
         <small id="emailHelp" className="form-text text-danger">{touched.name && errors.name ? errors.name : ''}</small>
      </div>
      <div className="form-group col-md-6">
        <input
          type="email"
          className="form-control"
          name="email"
          id="email"
          value={values.email}
          onChange={handleChange}
          onBlur={handleBlur}
          placeholder="E-mail"/>
        <small id="emailHelp" className="form-text text-danger">{touched.email && errors.email ? errors.email : ''}</small>
      </div>
    </div>
    <div className="form-group">
      <textarea 
        className="form-control" 
        rows="3" 
        name="text" 
        id="text"
        value={values.text}
        onChange={handleChange}
        onBlur={handleBlur}
        placeholder="Escreva um comentário">
      </textarea>
      <small id="emailHelp" className="form-text text-danger">{touched.text && errors.text ? errors.text : ''}</small>
    </div>
    <button className="btn btn-primary" type="submit" disabled={!dirty || isSubmitting}>{isSubmitting ? 'Enviando ...' : 'Enviar'}</button>
    </form>
  );
}

const CommentBox = withFormik({
  validationSchema: validationSchema,
  enableReinitialize: true,
  mapPropsToValues: () => ({ name: '' , email: '', text: ''}),
  handleSubmit: (values, { resetForm, setErrors, setSubmitting }) => {
    let data = Object.assign(values, {'article_id': window.article_id, '_xsrf': getCookie('_xsrf')});
    setSubmitting(true);
    axios({
      method: "POST",
      url: "/comment/add",
      data: qs.stringify(data),
    }).then((response)=>{
      resetForm()
    }).catch((error) => {
      setSubmitting(false);
    })
  },
  displayName: 'BasicForm',
})(CommentForm);

export { CommentBox };
