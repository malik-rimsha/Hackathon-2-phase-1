# Research Findings: Todo Organization & Usability

## Decision: Priority representation
- **Decision**: Use Enum (Priority.HIGH/MEDIUM/LOW) for priority representation
- **Rationale**: Enum provides type safety, better autocomplete, and clean comparison operations. It also makes the code more maintainable and less prone to errors from typos in string values.
- **Alternatives considered**: 
  - String values ("high"/"medium"/"low"): More flexible but less type-safe and more prone to errors
  - Integer values (1/2/3): More compact but less readable and self-documenting

## Decision: Tags representation
- **Decision**: Use List[str] (multiple tags per task) for tags representation
- **Rationale**: Allows flexible multi-tagging (e.g., #work #urgent) and better usability. Users can categorize tasks by multiple criteria simultaneously.
- **Alternatives considered**:
  - Single string (one category): Simpler but too restrictive for real-world use cases
  - Set[str]: Would prevent duplicate tags but might be more complex for users

## Decision: Filter and search implementation
- **Decision**: Implement unified "view" command with optional parameters
- **Rationale**: Keeps interface simple and consistent. Users have one command to remember with various filtering options.
- **Alternatives considered**:
  - Separate filter and search commands: More explicit but would clutter the command interface
  - Sub-menu approach: More organized but requires more navigation steps

## Decision: Sorting strategy
- **Decision**: Implement non-destructive sorting (returns sorted view without mutating original list)
- **Rationale**: Preserves original order and avoids side effects. Users can sort temporarily without permanently changing the task order.
- **Alternatives considered**:
  - Sort in-place (mutate list): Changes the original order which might be unexpected for users
  - Toggle sort state: More complex to implement and manage

## Decision: Display indicators
- **Decision**: Use text symbols (![H], [M], [L]) for priority indicators
- **Rationale**: Text symbols are console-safe and readable in all terminals. They're also more accessible than emojis which might not render consistently across all systems.
- **Alternatives considered**:
  - Emojis (🔴🟡🟢): More visually appealing but might not render consistently across all terminals
  - Numbers (1, 2, 3): Less intuitive than letter abbreviations

## Implementation approach for extending existing code
- **Decision**: Extend existing Task data model and TodoList class rather than creating new structures
- **Rationale**: Maintains backward compatibility with existing Basic Level features. Follows the principle of extending rather than replacing existing functionality.
- **Implementation plan**:
  1. Extend Task model with priority and tags attributes
  2. Add methods to TodoList for managing priority and tags
  3. Implement search and filter logic
  4. Implement non-destructive sorting
  5. Update display/printing logic for indicators and tags
  6. Extend CLI menu/commands to expose new features