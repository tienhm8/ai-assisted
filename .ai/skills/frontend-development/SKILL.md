---
name: frontend-development
description: Develop and maintain frontend applications, pages, components, forms, state management and user interactions following approved UI/UX, architecture and security standards.
---

# Frontend Development Skill

## 1. Objective

Build user-friendly, accessible, responsive, maintainable
and testable frontend applications.

## 2. Required Inputs

- Functional Requirements
- UI/UX Design
- Design System
- API Specification
- Architecture Documents
- Authentication and RBAC Requirements
- Existing Frontend Code
- Coding Rules

## 3. Development Workflow

### Step 1: Analyze Requirements

Identify:
- Target users
- User journeys
- Pages and screens
- UI components
- Form requirements
- Data displayed
- User interactions
- Loading and error states
- Permission-dependent UI behavior

### Step 2: Inspect Existing Frontend

Review:
- Framework and version
- Application structure
- Routing
- Component conventions
- Styling approach
- State management
- API client
- Existing reusable components

Reuse existing components where appropriate.

### Step 3: Plan UI Structure

Define:
- Page structure
- Layout
- Shared components
- Feature components
- Data flow
- State boundaries
- Responsive behavior

### Step 4: Implement Components

Follow:
- Single responsibility
- Reusability
- Consistent naming
- Clear component interfaces
- Typed props
- Appropriate composition

Avoid unnecessarily large components.

### Step 5: Implement Forms

Every form should consider:
- Input validation
- Required fields
- Error messages
- Loading state
- Submission state
- Duplicate submission prevention
- Success feedback
- Server-side validation errors

Client-side validation must not replace backend validation.

### Step 6: Integrate APIs

- Follow API specifications.
- Use typed request and response models.
- Handle HTTP errors.
- Handle network failures.
- Handle loading states.
- Avoid duplicate requests where inappropriate.
- Do not expose secrets.

### Step 7: Handle Authentication and Permissions

- Follow approved authentication flows.
- Display actions according to permissions.
- Handle expired sessions.
- Handle unauthorized responses.
- Never treat hidden UI as backend authorization.

### Step 8: Accessibility and Responsive Design

Consider:
- Semantic HTML
- Keyboard navigation
- Focus management
- Accessible labels
- Contrast
- Mobile layouts
- Tablet layouts
- Desktop layouts

### Step 9: Performance Optimization

Evaluate:
- Unnecessary re-renders
- Bundle size
- Image optimization
- Lazy loading
- Server/client rendering boundaries
- Data fetching strategy

### Step 10: Test

Write appropriate:
- Component tests
- Form tests
- Interaction tests
- Responsive tests
- Accessibility checks
- E2E tests where applicable

## 4. Output Format

Produce:
1. Pages and Components
2. Component Structure
3. API Integrations
4. State Management
5. Form Validation
6. Permission Handling
7. Responsive Behavior
8. Error and Loading States
9. Tests
10. Documentation Updates

## 5. Quality Checklist

- [ ] UI matches approved requirements.
- [ ] Existing design system is reused.
- [ ] Components are maintainable.
- [ ] TypeScript types are defined.
- [ ] Forms are validated.
- [ ] API errors are handled.
- [ ] Loading states are handled.
- [ ] Permission-dependent actions are handled.
- [ ] Responsive layouts work.
- [ ] Accessibility is considered.
- [ ] No secrets are exposed.
- [ ] Tests pass.

## 6. Restrictions

- Do not invent business behavior.
- Do not bypass backend authorization.
- Do not introduce unnecessary UI libraries.
- Do not duplicate shared components.
- Do not change global design conventions without approval.
- Do not put sensitive business logic only in the frontend.

## 7. Definition of Done

- UI implementation completed.
- API integration completed.
- Validation implemented.
- Loading and error states implemented.
- Responsive behavior verified.
- Relevant tests passed.
- Code review completed.

## 8. Delivery Report

Report:
- Pages created or modified
- Components created or modified
- APIs integrated
- State management changes
- Tests executed
- Known limitations
