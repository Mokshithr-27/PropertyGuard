/**
 * PropertyGuard Root Application Component
 * Wraps application routing tree within the React Router DOM BrowserRouter provider.
 */

import { BrowserRouter as Router } from 'react-router-dom';
import AppRoutes from './routes/AppRoutes';

function App() {
  return (
    <Router>
      <AppRoutes />
    </Router>
  );
}

export default App;
