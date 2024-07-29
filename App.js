import React, { useState } from 'react';
import axios from 'axios';
import CodeEditor from './components/CodeEditor';
import SuggestionsPanel from './components/SuggestionsPanel';

function App() {
  const [code, setCode] = useState('');
  const [suggestions, setSuggestions] = useState([]);
  const [debugHelp, setDebugHelp] = useState('');
  const [tips, setTips] = useState('');

  const fetchSuggestions = async () => {
    try {
      const response = await axios.post('/api/suggest', { code });
      setSuggestions(response.data);
    } catch (error) {
      console.error('Error fetching suggestions:', error);
    }
  };

  const fetchDebugHelp = async () => {
    try {
      const response = await axios.post('/api/debug', { code });
      setDebugHelp(response.data);
    } catch (error) {
      console.error('Error fetching debug help:', error);
    }
  };

  const fetchTips = async () => {
    try {
      const response = await axios.post('/api/tips', { code });
      setTips(response.data);
    } catch (error) {
      console.error('Error fetching tips:', error);
    }
  };

  return (
    <div className="App">
      <CodeEditor code={code} setCode={setCode} />
      <button onClick={fetchSuggestions}>Get Suggestions</button>
      <button onClick={fetchDebugHelp}>Get Debugging Help</button>
      <button onClick={fetchTips}>Get Tips</button>
      <SuggestionsPanel suggestions={suggestions} debugHelp={debugHelp} tips={tips} />
    </div>
  );
}

export default App;
