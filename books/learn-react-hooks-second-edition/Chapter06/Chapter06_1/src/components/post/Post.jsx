import { PropTypes } from 'prop-types'
import { useContext } from 'react'
import { ThemeContext } from '@/contexts/ThemeContext.js'

export function Post({ title, content, author }) {
  const theme = useContext(ThemeContext)
  return (
    <div>
      <h3 style={{ color: theme.primaryColor }}>{title}</h3>
      <div>{content}</div>
      <br />
      <i>
        Written by <b>{author}</b>
      </i>
    </div>
  )
}

Post.propTypes = {
  title: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  author: PropTypes.string.isRequired,
}