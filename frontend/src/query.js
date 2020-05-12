import gql from "graphql-tag";
// our first query will requests all movies
// with only given fields
// note the usage of gql with jsvascript string literal

export const ARTISTS_LIST_QUERY = gql`
    query artists{
        artists{
            name, artistPoster
        }
    }
`
// Note the usage of argument.
// the exclamation mark makes the slug argument as required
// without it , argument will be optional
export const ARTIST_QUERY = gql`
    query artist($slug:String!){
        artist(slug:$slug){
            id, name, artistPoster, slug
        }
    }
`