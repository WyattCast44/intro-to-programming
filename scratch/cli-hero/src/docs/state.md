# State

Most applications need some way to track data across commands, options, etc. CLIHero provides a simple in-memory store you can use for this.

## Using `State`

Using state is as simple as calling `state()` on any application instance. You can then insert, read, update, and delete data in the state.

#### Inserting Data

```python
Application().state().set('key', 'value')
```

#### Reading Data

```python
Application().state().get('key', 'defaultValue')
```

#### Updating Data

```python
Application().state().update('key', 'newValue')
```

#### Upsert Data

Upserting allows you to update a key if it already exists, or insert and set the key if it doesn't exist yet.

```python
Application().state().upsert('key', 'value')
```

#### Deleting Data

```python
Application().state().remove('key')
```

#### Checking State

```python
Application().state().has('key')
```