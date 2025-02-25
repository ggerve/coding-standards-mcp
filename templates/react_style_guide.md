# React Style Guide

## Component Naming
- Use PascalCase for components (`UserProfile`)
- Use camelCase for instances (`userProfile`)
- Use kebab-case for CSS files (`user-profile.css`)
- Use descriptive, clear names

## Component Structure
```tsx
// UserProfile.tsx
import { FC } from 'react'
import styles from './UserProfile.module.css'

interface UserProfileProps {
  name: string
  role?: string
}

export const UserProfile: FC<UserProfileProps> = ({
  name,
  role = 'User'
}) => (
  <div className={styles.container}>
    <h2>{name}</h2>
    <span>{role}</span>
  </div>
)
```

## Props
- Use TypeScript interfaces
- Document complex props
- Use default values
- Destructure props
- Keep props minimal

## Hooks
- Start with 'use' prefix
- Keep hooks simple
- Extract common logic
- Follow hook rules
- Handle cleanup

## State Management
- Keep state close to usage
- Lift state when needed
- Use context sparingly
- Prefer reducers for complex state
- Consider state libraries for large apps

## Event Handling
```tsx
// Do
const handleSubmit = (e: FormEvent) => {
  e.preventDefault()
  // Handle submit
}

// Don't
<button onClick={(e) => doSomething(e)}>
```

## Styling
- Use CSS modules
- Follow BEM naming
- Keep styles colocated
- Use CSS variables
- Avoid inline styles

## File Organization
```
components/
  Button/
    Button.tsx
    Button.module.css
    Button.test.tsx
    index.ts
```

## JSX
- One component per file
- Use fragments to avoid divs
- Self-close empty elements
- Use conditional rendering
- Keep JSX clean

## Testing
- Test component behavior
- Use meaningful test names
- Mock complex dependencies
- Test user interactions
- Write accessible tests
