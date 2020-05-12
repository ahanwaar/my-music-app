import React from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";
import { ApolloProvider } from 'react-apollo';
import ApolloClient from 'apollo-boost';
import { BrowserRouter } from 'react-router-dom'
import App from './App';

const client = new ApolloClient({
  uri: 'http://127.0.0.1:8000/graphql/',
});

ReactDOM.render(
	<BrowserRouter>
		<ApolloProvider client={client}>
			<App />
		</ApolloProvider>
	</BrowserRouter>,
	document.getElementById("root")
);

/// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: http://bit.ly/CRA-PWA
serviceWorker.unregister();